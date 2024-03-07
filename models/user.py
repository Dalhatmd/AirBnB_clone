""" Module to handle User Instances """
from .base_model import BaseModel


class User(BaseModel):
    """ User Class to handle system users """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
