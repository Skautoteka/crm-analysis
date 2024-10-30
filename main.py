from enum import Enum
from functools import lru_cache
from typing import Annotated, Optional

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


class Player(BaseModel):
    id: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    sex: Optional[str]
    age: Optional[int]


class Report(BaseModel):
    id: Optional[str]
    name: Optional[str]
    status: Optional[StatusEnum]
    player: Optional[Player]


app = FastAPI()
router = APIRouter()


@router.post("/filter-reports/")
def filter_reports(
    settings: Annotated[Settings, Depends(get_settings)],
    report: Report | None = None,
):
    try:
        response = requests.get(
            f"{settings.backend_url}report/all",
            timeout=0.1,
        )
    except (requests.ConnectionError, requests.Timeout) as err:
        return {
            "detail": str(err),
        }

    return responses.Response(
        content=response.text,
        media_type="application/json",
    )


app.include_router(router)
