#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
=======
from models.base_model import BaseModel
>>>>>>> 4709c26c3e0ffb5f7a3d179b9366091bfc4c0970
from models import storage_type
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
<<<<<<< HEAD
        id_state = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        id_state = ""
=======
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ""
>>>>>>> 4709c26c3e0ffb5f7a3d179b9366091bfc4c0970
        name = ""
