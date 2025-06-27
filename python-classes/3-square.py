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
        Retrieve private instance attribute: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set private instance attribute size.
        Raises TypeError if not int and ValueError if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square
        """
        return self.__size ** 2
