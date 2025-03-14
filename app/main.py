import json
import operator
from enum import Enum
from functools import lru_cache
from io import StringIO
from typing import Annotated, List, Optional

import polars as pl
import requests
from fastapi import APIRouter, Depends, FastAPI, HTTPException, responses
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
    player_id = "playerId"
    region_id = "regionId"
    team_id = "teamId"
    position = "position"
    sex = "sex"
    report_name = "report_name"

    reflex = "reflex"
    physical_strength = "physical_strength"
    speed = "speed"
    interceptions = "interceptions"
    versatility = "versatility"
    creativity = "creativity"
    finishing = "finishing"
    positioning = "positioning"
    heading = "heading"
    conditioning = "conditioning"
    stamina = "stamina"
    ball_control = "ball_control"
    passing = "passing"
    dribbling = "dribling"
    flexibility = "flexibility"
    line_play = "line_play"
    anticipation = "anticipation"
    one_on_one = "one_on_one"
    crossing = "crossing"
    playmaking = "playmaking"
    shot_accuracy = "shot_accuracy"
    playing_with_feet = "playing_with_feet"
    tackling = "tackling"
    throw_ins = "throw_ins"
    balance = "balance"
    game_vision = "game_vision"
    communication = "communication"
    offensive_support = "offensive_support"
    defensive_skills = "defensive_skills"
    responsibility = "responsibility"
    defensive_support = "defensive_support"
    off_ball_movement = "off_ball_movement"

    evaluation = "evaluation"


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
            raise HTTPException(status_code=502, detail=str(err)) from err
    else:
        try:
            response = requests.get(
                f"{settings.backend_url}note/all",
                timeout=0.1,
            )
        except (requests.ConnectionError, requests.Timeout) as err:
            raise HTTPException(status_code=502, detail=str(err)) from err

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"Status code of response is not OK: {response.status_code}",
        )

    if response.text == "":
        raise HTTPException(status_code=502, detail="Empty response")

    try:
        response_json = response.json()
    except json.JSONDecodeError as err:
        raise HTTPException(status_code=502, detail=str(err)) from err
    if "errorStatus" in response_json:
        if "message" in response_json:
            raise HTTPException(
                status_code=502, detail=response_json["message"]
            )
        else:
            raise HTTPException(status_code=502, detail=response.text)

    if response_json == []:
        return responses.Response(
            content=json.dumps([]),
            media_type="application/json",
        )

    df = pl.read_json(StringIO(response.text))

    # Find reports matching filters
    query = True
    if analyze_request.type == TypeEnum.report:
        # Report has to contain id, playerId, and traits has to contain traitId and value.
        try:
            _ = df.select(
                "id",
                "playerId",
                "traits",
            )
        except pl.exceptions.ColumnNotFoundError as err:
            raise HTTPException(
                status_code=502,
                detail="Fields: id, playerId, or traits not in report",
            ) from err
        try:
            _ = df.explode("traits").select(
                pl.col("traits").struct.field("traitId", "value")
            )
        except pl.exceptions.StructFieldNotFoundError as err:
            raise HTTPException(
                status_code=502,
                detail="Fields: traitId, or value not in report traits",
            ) from err

        if analyze_request.filters is not None:
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
                        KeyEnum.name,
                        KeyEnum.first_name,
                        KeyEnum.last_name,
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
                    elif request_filter.key == KeyEnum.position:  # TODO
                        query &= getattr(operator, request_filter.predicate)(
                            pl.col("player").struct.field("positionId"),
                            request_filter.value,
                        )
                    elif request_filter.key in [
                        KeyEnum.player_id,
                        KeyEnum.region_id,
                    ]:
                        query &= getattr(operator, request_filter.predicate)(
                            pl.col(request_filter.key), request_filter.value
                        )
                    else:
                        try:
                            value = int(request_filter.value)
                        except ValueError:
                            raise HTTPException(
                                status_code=502,
                                detail=f"value in filter is not int: {request_filter.value}",
                            )
                        query &= (
                            pl.col("traits").struct.field("traitId")
                            == request_filter.key.upper()
                        ) & (
                            getattr(operator, request_filter.predicate)(
                                pl.col("traits").struct.field("value"),
                                value,
                            )
                        )
                    # TODO: errors
                elif request_filter.predicate in [
                    PredicateEnum.avg_ge,
                    PredicateEnum.avg_gt,
                    PredicateEnum.avg_le,
                    PredicateEnum.avg_lt,
                    PredicateEnum.avg_eq,
                    PredicateEnum.avg_ne,
                ]:
                    continue
        ids = df.explode("traits").filter(query).select("id")
        ids_set = set(ids.to_dict()["id"])
        if analyze_request.filters is not None:
            for request_filter in analyze_request.filters:
                if request_filter.predicate not in [
                    PredicateEnum.avg_ge,
                    PredicateEnum.avg_gt,
                    PredicateEnum.avg_le,
                    PredicateEnum.avg_lt,
                    PredicateEnum.avg_eq,
                    PredicateEnum.avg_ne,
                ]:
                    continue
                try:
                    value = int(request_filter.value)
                except ValueError:
                    raise HTTPException(
                        status_code=502,
                        detail=f"value in filter is not int: {request_filter.value}",
                    )
                ids_set &= set(
                    df.filter(pl.col("id").is_in(ids))
                    .explode("traits")
                    .filter(
                        pl.col("traits").struct.field("traitId")
                        == request_filter.key.upper()
                    )
                    .group_by("playerId")
                    .agg(pl.col("traits").struct.field("value").mean(), "id")
                    .filter(
                        getattr(
                            operator,
                            request_filter.predicate[
                                request_filter.predicate.find("_") + 1 :
                            ],
                        )(
                            pl.col("value"),
                            value,
                        )
                    )
                    .explode("id")
                    .select("id")
                    .to_dict()["id"]
                )
    else:
        # Note has to contain id, playerNumber and evaluation.
        try:
            _ = df.select(
                "id",
                "playerNumber",
                "evaluation",
            )
        except pl.exceptions.ColumnNotFoundError as err:
            raise HTTPException(
                status_code=502,
                detail="Fields: id, playerNumber, or evaluation not in note",
            ) from err

        if analyze_request.filters is not None:
            for request_filter in analyze_request.filters:
                if request_filter.predicate in [
                    PredicateEnum.ge,
                    PredicateEnum.gt,
                    PredicateEnum.le,
                    PredicateEnum.lt,
                    PredicateEnum.eq,
                    PredicateEnum.ne,
                ]:
                    value = request_filter.value
                    if request_filter.key == KeyEnum.evaluation:
                        try:
                            value = int(request_filter.value)
                        except ValueError as err:
                            raise HTTPException(
                                status_code=502,
                                detail=f"value in filter is not int: {request_filter.value}",
                            ) from err
                    query &= getattr(operator, request_filter.predicate)(
                        pl.col(request_filter.key), value
                    )
        query &= pl.col("playerNumber").is_not_null()
        ids = df.filter(query).select("id")
        ids_set = set(ids.to_dict()["id"])
        if analyze_request.filters is not None:
            for request_filter in analyze_request.filters:
                if request_filter.predicate not in [
                    PredicateEnum.avg_ge,
                    PredicateEnum.avg_gt,
                    PredicateEnum.avg_le,
                    PredicateEnum.avg_lt,
                    PredicateEnum.avg_eq,
                    PredicateEnum.avg_ne,
                ]:
                    continue
                value = request_filter.value
                if request_filter.key == KeyEnum.evaluation:
                    try:
                        value = int(request_filter.value)
                    except ValueError as err:
                        raise HTTPException(
                            status_code=502,
                            detail=f"value in filter is not int: {request_filter.value}",
                        ) from err
                ids_set &= set(
                    df.filter(pl.col("id").is_in(ids))
                    .group_by("playerNumber")
                    .agg(pl.col(request_filter.key).mean(), "id")
                    .filter(
                        getattr(
                            operator,
                            request_filter.predicate[
                                request_filter.predicate.find("_") + 1 :
                            ],
                        )(
                            pl.col(request_filter.key),
                            value,
                        )
                    )
                    .explode("id")
                    .select("id")
                    .to_dict()["id"]
                )

    # Construct content from reports/notes matching filters
    if analyze_request.type == TypeEnum.report:
        content = pl.Series(
            df.filter(pl.col("id").is_in(ids_set))
            .group_by("playerId")
            .agg(pl.col("id").alias("related"))
            .with_columns(values=[])
        ).to_list()
        for key in [
            "REFLEX",
            "PHYSICAL_STRENGTH",
            "SPEED",
            "INTERCEPTIONS",
            "VERSATILITY",
            "CREATIVITY",
            "FINISHING",
            "POSITIONING",
            "HEADING",
            "CONDITIONING",
            "STAMINA",
            "BALL_CONTROL",
            "PASSING",
            "DRIBBLING",
            "FLEXIBILITY",
            "LINE_PLAY",
            "ANTICIPATION",
            "ONE_ON_ONE",
            "CROSSING",
            "PLAYMAKING",
            "SHOT_ACCURACY",
            "PLAYING_WITH_FEET",
            "TACKLING",
            "THROW_INS",
            "BALANCE",
            "GAME_VISION",
            "COMMUNICATION",
            "OFFENSIVE_SUPPORT",
            "DEFENSIVE_SKILLS",
            "RESPONSIBILITY",
            "DEFENSIVE_SUPPORT",
            "OFF_BALL_MOVEMENT",
        ]:
            avg = pl.Series(
                df.explode("traits")
                .filter(
                    (pl.col("id").is_in(ids))
                    & (pl.col("traits").struct.field("traitId") == key)
                )
                .group_by("playerId")
                .agg(
                    pl.col("traits")
                    .struct.field("value")
                    .mean()
                    .alias("average")
                )
            ).to_list()
            for i, content_player in enumerate(content):
                for player in avg:
                    if content_player["playerId"] != player["playerId"]:
                        continue
                    content[i]["values"].append(
                        {"name": key, "average": player["average"]}
                    )
            latest_times = pl.Series(
                df.explode("traits")
                .filter(
                    (pl.col("id").is_in(ids))
                    & (pl.col("traits").struct.field("traitId") == key)
                )
                .group_by("playerId")
                .agg(
                    pl.col("traits")
                    .struct.field("updatedAt")
                    .sort(descending=True)
                    .first()
                )
            ).to_list()
            for player in latest_times:
                try:
                    latest_value = pl.Series(
                        df.explode("traits")
                        .filter(
                            (pl.col("playerId") == player["playerId"])
                            & (pl.col("traits").struct.field("traitId") == key)
                            & (
                                pl.col("traits").struct.field("updatedAt")
                                == player["updatedAt"]
                            )
                        )
                        .select(pl.col("traits").struct.field("value"))
                    ).to_list()[0]
                except IndexError:
                    continue
                for i, content_player in enumerate(content):
                    if content_player["playerId"] != player["playerId"]:
                        continue
                    for j, value in enumerate(content[i]["values"]):
                        if value["name"] != key:
                            continue
                        content[i]["values"][j].update(
                            {"latestValue": latest_value}
                        )
    else:
        content = pl.Series(
            df.filter(pl.col("id").is_in(ids_set))
            .group_by("playerNumber")
            .agg(pl.col("id").alias("related"))
            .with_columns(values=[])
        ).to_list()
        avg = pl.Series(
            df.group_by("playerNumber").agg(
                pl.col("evaluation").mean().alias("average")
            )
        ).to_list()
        for i, content_player in enumerate(content):
            for player in avg:
                if content_player["playerNumber"] != player["playerNumber"]:
                    continue
                content[i]["values"].append(
                    {"name": "evaluation", "average": player["average"]}
                )
        latest_times = pl.Series(
            df.group_by("playerNumber").agg(
                pl.col("updatedAt").sort(descending=True).first()
            )
        ).to_list()
        for player in latest_times:
            if player["playerNumber"] is None:
                continue
            try:
                latest_value = pl.Series(
                    df.filter(
                        (pl.col("playerNumber") == player["playerNumber"])
                        & (pl.col("updatedAt") == player["updatedAt"])
                    ).select(pl.col("evaluation"))
                ).to_list()[0]
            except IndexError:
                continue
            for i, content_player in enumerate(content):
                if content_player["playerNumber"] != player["playerNumber"]:
                    continue
                for j, value in enumerate(content[i]["values"]):
                    content[i]["values"][j].update(
                        {"latestValue": latest_value}
                    )
    # TODO uuid

    return responses.Response(
        content=json.dumps(content),
        media_type="application/json",
    )


app.include_router(router)
