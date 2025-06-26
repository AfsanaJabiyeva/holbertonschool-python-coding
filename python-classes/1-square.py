#!/usr/bin/python3
"""
This module defines Square class where
size should be integer and greater than 0
"""


class Square:
    """This class defines a square with a private size attribute."""


def __init__(self, size=0):
    """
    Initialize new Square instance
    Rsises TypeError if size is not int and ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size
