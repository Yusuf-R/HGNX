#!/usr/bin/env python3
"""This the base template for all GroupEvents object instances."""

from models.parent import Parent, Base
from sqlalchemy import Column, ForeignKey, String


class GroupEvents(Parent, Base):
    """GroupEvents class"""
    __tablename__ = "group_events"
    group_id = Column(String(60), ForeignKey("groups.id"), nullable=False)
    event_id = Column(String(60), ForeignKey("events.id"), nullable=False)
