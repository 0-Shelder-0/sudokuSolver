from typing import Optional

from sqlalchemy.orm import Session

from webapi import models
from webapi.models import Solution
from webapi.schemas.solution_status import SolutionStatusCreate


def get_last_status(db: Session, solution_id: int) -> Optional[models.SolutionStatus]:
    return db.query(models.SolutionStatus) \
        .filter(models.SolutionStatus.solution_id == solution_id) \
        .order_by(models.SolutionStatus.created_at.desc()) \
        .first()


def create_status(db: Session, solution_status: SolutionStatusCreate) -> models.SolutionStatus:
    db_status = models.SolutionStatus(solution_id=solution_status.solution_id,
                                      status=int(solution_status.status),
                                      created_at=solution_status.created_at)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def get_solution_by_id(db: Session, solution_id: int) -> Optional[models.Solution]:
    return db.query(models.Solution).filter(models.Solution.id == solution_id).first()


def get_solution_by_text(db: Session, solution: str) -> Optional[models.Solution]:
    return db.query(models.Solution).filter(models.Solution.solution == solution).first()


def create_solution(db: Session, solution_text: str) -> models.Solution:
    db_solution = models.Solution(solution=solution_text)
    db.add(db_solution)
    db.commit()
    db.refresh(db_solution)
    return db_solution


def update_solution(db: Session, solution_id: int, solution_text: str) -> Optional[Solution]:
    solution = get_solution_by_id(db, solution_id=solution_id)

    if solution is None:
        return None

    solution.solution = solution_text
    db.commit()
    db.refresh(solution)
    db.query(models.Solution) \
        .filter(models.Solution.id == solution_id) \
        .update({'solution': solution_text})
    db.commit()
    return solution
