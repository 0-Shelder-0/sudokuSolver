from pydantic import BaseModel


class Solution(BaseModel):
    solution: [[]]


class SolutionCreate(Solution):
    pass


class SolutionUpdate(Solution):
    id: int


class SolutionIdResponse(BaseModel):
    solution_id: int


class SolutionResponse(Solution):
    solution_id: int
