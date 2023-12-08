#!/usr/bin/python3
"""
Module containing the BaseModel class.

Defines the BaseModel class, which serves as the base class for other classes.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for other classes.

    Public instance attributes:
    - id (str): Assigned with a unique ID using uuid.uuid4().
    - created_at (datetime): Current datetime when an instance is created.
    - updated_at (datetime): Current datetime when an instance is created
      and updated every time the object changes.

    Public instance methods:
    - __str__(self): Returns a string representation of the object.
    - save(self): Updates the public instance attribute 'updated_at'
    with the current datetime.
    - to_dict(self): Returns a dictionary
    containing all keys/values of __dict__ of the instance.

    Usage:
    >>> my_model = BaseModel()
    >>> print(my_model)
    [BaseModel] (unique_id)
    {'id': 'unique_id', 'created_at': 'ISO_datetime',
    'updated_at': 'ISO_datetime'}
    >>> my_model.save()
    >>> my_model_json = my_model.to_dict()
    >>> print(my_model_json)
    {'id': 'unique_id', 'created_at':
    'ISO_datetime', 'updated_at': 'ISO_datetime', '__class__': 'BaseModel'}
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes instance attributes.

        Args:
            *args: Variable length argument list (not used in this case).
            **kwargs: Keyword args to initialize attributes from a dictionary.
        """
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
                )
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
                )
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing keys/values of the instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A formatted string.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        and saves the object to the storage.
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
