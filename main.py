from enum import Enum

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


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
def filter_reports(report: Report):
    return {}


app.include_router(router)
