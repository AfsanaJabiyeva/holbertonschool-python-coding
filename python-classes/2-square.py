#!/usr/bin/python3
"""
This module defines the Square class where
size must be an integer and greater than or equal to 0.
"""


class Square:
    """This class defines a square with a private size attribute."""
    def __init__(self, size=0):
        """
        Initialize a new square instance
        Raises typeerror if not int and valuerror if less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area
        """
        return self.__size ** 2
