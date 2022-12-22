from datetime import datetime

from pydantic import BaseModel


class SolutionStatus(BaseModel):
    solution_id: int
    status: int
    created_at: datetime


class SolutionStatusCreate(SolutionStatus):
    pass


class SolutionStatusInDb(SolutionStatus):
    id: int

    class Config:
        orm_mode = True
