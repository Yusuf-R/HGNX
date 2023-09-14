#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.parent import Parent, Base
from sqlalchemy import Column, String


class User(Parent, Base):
    """User class"""
    __tablename__ = "users"
    name = Column(String(32), unique=True, nullable=False)
