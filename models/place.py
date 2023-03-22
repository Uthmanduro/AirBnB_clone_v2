#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import storage_type
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.review import Review
from models.amenity import Amenity

if storage_type == 'db':
    place_amenity =\
        Table('place_amenity', Base.metadata,
              Column('place_id', String(60),
                     ForeignKey('places.id', onupdate='CASCADE',
                                ondelete='CASCADE'),
                     primary_key=True, nullable=False),
              Column('amenity_id', String(60),
                     ForeignKey('amenities.id', onupdate='CASCADE',
                                ondelete='CASCADE'),
                     primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if storage_type == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024),  nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship('Review',
                               cascade="all, delete", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="places")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if storage_type != "db":
        @property
        def reviews(self):
            """returns the list of Review
                instances with place_id equals to the current Place.id
            """
            from models import storage
            list_reviews = []
            reviews_all = storage.all(Review)
            for rev in reviews_all.values():
                if rev.place_id == self.id:
                    list_reviews.append(rev)
            return list_reviews

        def amenities(self):
            """returns the list of Review
                instances with place_id equals to the current Place.id
            """
            from models import storage
            list_amenities = []
            amenities_all = storage.all(Amenity)
            for rev in amenities_all.values():
                if rev.place_id == self.id:
                    list_amenities.append(rev)
            return list_amenities
