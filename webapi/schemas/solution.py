from typing import List

from pydantic import BaseModel


class SolutionModel(BaseModel):
    solution: List[List[int]]


class SolutionCreate(SolutionModel):
    pass


class SolutionUpdate(SolutionModel):
    pass


class SolutionIdResponse(BaseModel):
    solution_id: int


class SolutionResponse(SolutionModel):
    solution_id: int
