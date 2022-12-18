from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Solution(Base):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index=True)
    solution = Column(String, nullable=False)


class SolutionStatus(Base):
    __tablename__ = "solution_statuses"

    id = Column(Integer, primary_key=True, index=True)
    solution_id = Column(Integer, ForeignKey(Solution.id), nullable=False)
    status = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    solution = relationship('solutions', foreign_keys='solution_statuses.solution_id')
