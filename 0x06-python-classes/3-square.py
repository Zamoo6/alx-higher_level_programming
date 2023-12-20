#!/usr/bin/python3
"""Square class defining."""
class Square:
    """square representing."""
    def __init__(self, size=0):
        """square initializing."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """square resulting."""
        return (self.__size * self.__size)i
