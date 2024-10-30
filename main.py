from enum import Enum
from functools import lru_cache
from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI
from pydantic import BaseModel

from .config import Settings


@lru_cache
def get_settings():
    return Settings()


class StatusEnum(str, Enum):
    in_progress = "IN_PROGRESS"
    completed = "COMPLETED"


class Player(BaseModel):
    id: str
    firstName: str
    lastName: str
    sex: str
    age: int


class Report(BaseModel):
    id: str
    name: str
    status: StatusEnum
    player: Player


app = FastAPI()
router = APIRouter()


@router.post("/filter-reports/")
def filter_reports(
    settings: Annotated[Settings, Depends(get_settings)],
    report: Report,
):
    return {}


app.include_router(router)
