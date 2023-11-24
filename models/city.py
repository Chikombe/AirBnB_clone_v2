#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    storage_type = "db"

    def __init__(self, storage_type="db", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage_type = storage_type

        if storage_type == 'db':
            name = Column(String(128), nullable=False)
            id_state = Column(String(60), ForeignKey('states.id'), nullable=False)
            places = relationship('Place', backref='cities',
                    cascade='all, delete, delete-orphan')
        else:
            id_state = ""
            name = ""
