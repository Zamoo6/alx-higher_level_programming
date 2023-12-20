#!/usr/bin/python3
"""square class defining."""
class Square:
    """square represnting"""
    def __init__(self, size=0):
        """square initializing"""
        self.size = size

    @property
    def size(self):
        """square def1"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """squsr def2"""
        return self.__size * self.__size
