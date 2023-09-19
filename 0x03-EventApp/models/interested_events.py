#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.parent import Parent, Base
from sqlalchemy import Column, String, ForeignKey


class InterestedEvents(Parent, Base):
    """InterestedEvents class"""
    __tablename__ = "interested_events"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    event_id = Column(String(60), ForeignKey("events.id"), nullable=False)
