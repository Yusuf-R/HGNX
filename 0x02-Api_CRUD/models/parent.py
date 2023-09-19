#!/usr/bin/env python3
"""The base Model class."""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class Parent:
    """Base class for all child class."""

    id = Column(
        String(60), nullable=False, primary_key=True, default=uuid.uuid4
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize
        :param args: arguments
        :param kwargs: keyword arguments

        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """String representation of the class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def to_dict(self):
        """Dictionary representation of the class"""
        obj_dict = self.__dict__.copy()
        # obj_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        return obj_dict

    def save(self):
        """Save object instance to database"""
        from models import storage

        storage.new(self)
        storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
        storage.save()
