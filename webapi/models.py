from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Solution(Base):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index=True)
    solution = Column(String, nullable=False)
    statuses = relationship("SolutionStatus", back_populates="solution")


class SolutionStatus(Base):
    __tablename__ = "solution_statuses"

    id = Column(Integer, primary_key=True, index=True)
    solution_id = Column(Integer, ForeignKey(Solution.id), nullable=False)
    status = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    solution = relationship("Solution", back_populates="statuses")
