""" Module to handle Review Instances """
from .base_model import BaseModel


class Review(BaseModel):
    """ Review Class to handle system Reviews """

    place_id = ""
    user_id = ""
    text = ""
