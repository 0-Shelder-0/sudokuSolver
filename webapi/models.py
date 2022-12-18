from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Solution(Base):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index=True)
    solution = Column(String)


class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    solution_id = Column(Integer, ForeignKey(Solution.id))
    status = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    solution = relationship('solutions', foreign_keys='statuses.solution_id')
