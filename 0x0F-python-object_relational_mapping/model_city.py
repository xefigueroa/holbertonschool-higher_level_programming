#!/usr/bin/python3
"""Defines class city"""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base, State


class City(Base):
    """Represents a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
