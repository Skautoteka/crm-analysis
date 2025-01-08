import json
import operator
from enum import Enum
from functools import lru_cache
from io import StringIO
from typing import Annotated, List, Optional

import polars as pl
import requests
from fastapi import APIRouter, Depends, FastAPI, responses
from pydantic import BaseModel

from .config import Settings


@lru_cache
def get_settings():
    return Settings()


class StatusEnum(str, Enum):
    in_progress = "IN_PROGRESS"
    completed = "COMPLETED"


class PositionEnum(str, Enum):
    forward = "FORWARD"
    defense = "DEFENSE"
    winger = "WINGER"


class TypeEnum(str, Enum):
    note = "note"
    report = "report"


class KeyEnum(str, Enum):
    team = "team"
    first_name = "firstName"
    last_name = "lastName"
    name = "name"
    player_number = "player_number"
    position = "position"
    sex = "sex"
    report_name = "report_name"
    reflex = "reflex"
    speed = "speed"
    interceptions = "interceptions"
    finishing = "finishing"
    stamina = "stamina"
    heading = "heading"
    physical_strength = "physical_strength"


class PredicateEnum(str, Enum):
    lt = "lt"
    le = "le"
    gt = "gt"
    ge = "ge"
    eq = "eq"
    ne = "ne"
    avg_lt = "avg_lt"
    avg_le = "avg_le"
    avg_gt = "avg_gt"
    avg_ge = "avg_ge"
    avg_eq = "avg_eq"
    avg_ne = "avg_ne"


class Player(BaseModel):
    id: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    sex: str | None = None
    age: int | None = None
    position: PositionEnum | None = None


class Report(BaseModel):
    id: str | None = None
    name: str | None = None
    status: StatusEnum | None = None
    player: Player | None = None
    playerId: str | None = None


class Trait(BaseModel):
    name: str
    descending: bool = True
    minValue: int = 0
    maxValue: int = 10


class Mean(BaseModel):
    report: Report | None = None
    trait: Trait


class Filter(BaseModel):
    key: KeyEnum
    predicate: PredicateEnum
    value: str


class AnalyzeRequest(BaseModel):
    type: TypeEnum
    filters: Optional[List[Filter]] = None


app = FastAPI()
router = APIRouter()


@router.post("/filter-reports/")
def filter_reports(
    settings: Annotated[Settings, Depends(get_settings)],
    report: Report | None = None,
):
    try:
        response = requests.get(
            f"{settings.backend_url}report/all-detailed",
            timeout=0.1,
        )
    except (requests.ConnectionError, requests.Timeout) as err:
        return {
            "detail": str(err),
        }

    if report is None:
        return responses.Response(
            content=response.text,
            media_type="application/json",
        )

    df = pl.read_json(StringIO(response.text))

    query = True
    for k, v in report.model_dump().items():
        if k == "player":
            continue
        if v is None:
            continue
        query &= pl.col(k) == v
    if report.player is not None:
        for k, v in report.player.model_dump().items():
            if v is None:
                continue
            query &= pl.col("player").struct.field(k) == v

    return responses.Response(
        content=df.filter(query).write_json(),
        media_type="application/json",
    )


@router.post("/mean/")
def mean(
    settings: Annotated[Settings, Depends(get_settings)],
    mean: Mean,
):
    try:
        response = requests.get(
            f"{settings.backend_url}report/all-detailed",
            timeout=0.1,
        )
    except (requests.ConnectionError, requests.Timeout) as err:
        return {
            "detail": str(err),
        }

    df = pl.read_json(StringIO(response.text))

    query = pl.col("traits").struct.field("name") == mean.trait.name
    report = mean.report
    if report is not None:
        for k, v in report.model_dump().items():
            if k == "player":
                continue
            if v is None:
                continue
            query &= pl.col(k) == v
        if report.player is not None:
            for k, v in report.player.model_dump().items():
                if v is None:
                    continue
                query &= pl.col("player").struct.field(k) == v

    content = (
        df.explode("traits")
        .filter(query)
        .group_by("playerId")
        .agg(pl.col("traits").struct.field("value").mean())
        .filter(
            (pl.col("value") >= mean.trait.minValue)
            & (pl.col("value") < mean.trait.maxValue)
        )
        .sort("value", descending=mean.trait.descending)
        .write_json()
    )

    return responses.Response(
        content=content,
        media_type="application/json",
    )


@router.post("/analyze/")
def analyze(
    settings: Annotated[Settings, Depends(get_settings)],
    analyze_request: AnalyzeRequest,
):
    if analyze_request.type == TypeEnum.report:
        try:
            response = requests.get(
                f"{settings.backend_url}report/all-detailed",
                timeout=0.1,
            )
        except (requests.ConnectionError, requests.Timeout) as err:
            return {
                "detail": str(err),
            }
    else:
        try:
            response = requests.get(
                f"{settings.backend_url}note/all",
                timeout=0.1,
            )
        except (requests.ConnectionError, requests.Timeout) as err:
            return {
                "detail": str(err),
            }

    df = pl.read_json(StringIO(response.text))

    if analyze_request.filters is None or analyze_request.filters == []:
        content = pl.Series(
            df.group_by("playerId")
            .agg(pl.col("id").alias("related"))
            .with_columns(
                values=[],
            )
        ).to_list()
        return responses.Response(
            content=json.dumps(content),
            media_type="application/json",
        )

    query = True
    for request_filter in analyze_request.filters:
        if request_filter.predicate in [
            PredicateEnum.ge,
            PredicateEnum.gt,
            PredicateEnum.le,
            PredicateEnum.lt,
            PredicateEnum.eq,
            PredicateEnum.ne,
        ]:
            if request_filter.key in [
                KeyEnum.position,
                KeyEnum.name,
                KeyEnum.first_name,
                KeyEnum.last_name,
                KeyEnum.position,
                KeyEnum.sex,
            ]:
                query &= getattr(operator, request_filter.predicate)(
                    pl.col("player").struct.field(request_filter.key),
                    request_filter.value,
                )
            elif request_filter.key == KeyEnum.report_name:
                query &= getattr(operator, request_filter.predicate)(
                    pl.col("name"), request_filter.value
                )
            else:
                query &= getattr(operator, request_filter.predicate)(
                    pl.col(request_filter.key), request_filter.value
                )
            # TODO: errors
    df.filter(query)
    content = pl.Series(
        df.filter(query)
        .group_by("playerId")
        .agg(pl.col("id").alias("related"))
        .with_columns(
            values=[],
        )
    ).to_list()

    return responses.Response(
        content=json.dumps(content),
        media_type="application/json",
    )


app.include_router(router)
