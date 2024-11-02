#!/usr/bin/python3
"""
This module defines the Base class
"""

class Base:
    """
    Base class for managing the 'id' attribute across all future classes

    Attributes:
    __nb_objects (int): A Private class attribute that counts the number of objects
    """

    __nb_object = 0
    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        
        Args:
        id (int, optional): If provided assigns the value to the instance's id attribute.
                            Otherwise, increments __nb_objects and assigns its value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
