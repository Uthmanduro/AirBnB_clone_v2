#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id
                equals to the current State.id
            """
            from models import storage
            list_city = []
            cities_all = storage.all(City)
            for cty in cities_all.values():
                if cty.state_id == self.id:
                    list_city.append(cty)
            return list_city

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
