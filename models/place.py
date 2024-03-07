""" Module to handle Place Instances """
from .base_model import BaseModel


class Place(BaseModel):
    """ Place Class to handle system Places """

    name = ""
    amenity_ids = []
    longitude = 0.0
    latitude = 0.0
    price_by_night = 0
    max_guest = 0
    number_bathrooms = 0
    number_rooms = 0
    description = ""
    city_id = ""
    user_id = ""
