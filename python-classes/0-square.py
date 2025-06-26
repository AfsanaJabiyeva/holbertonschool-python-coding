#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
"""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

            size: The size of the square (no type/value verification yet).
        """
        self.__size = size
