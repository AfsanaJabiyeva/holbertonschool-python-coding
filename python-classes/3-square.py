#!/usr/bin/python3
"""
This module defines the Square class where
size must be an integer and greater than or equal to 0.
Setter and getter properties
"""


class Square:
    """This class defines a square with a private size attribute."""
    def __init__(self, size=0):
        """
        Initialize a new square instance
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve Private instance attribute: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter to set private instance attribute
        Raises typeerror if not int and valuerror if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area
        """
        return self.__size ** 2
