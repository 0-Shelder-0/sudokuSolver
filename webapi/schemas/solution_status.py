from datetime import datetime

from pydantic import BaseModel


class SolutionStatusModel(BaseModel):
    solution_id: int
    status: int
    created_at: datetime


class SolutionStatusCreate(SolutionStatusModel):
    pass


class SolutionStatusInDb(SolutionStatusModel):
    id: int

    class Config:
        orm_mode = True
