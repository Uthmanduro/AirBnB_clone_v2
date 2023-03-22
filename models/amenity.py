#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class model"""
    if storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
