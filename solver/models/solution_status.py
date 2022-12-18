from solver.models.status import Status


class SolutionStatusCreate:
    solution_id: int
    status: Status

    def __init__(self, solution_id: int, status: Status):
        self.solution_id = solution_id
        self.status = status
