#!/usr/bin/python3
"""State Model module"""
from models.__init__ import storage
from models.base_model import BaseModel


class State(BaseModel):
    """The state class"""
    name = ""
