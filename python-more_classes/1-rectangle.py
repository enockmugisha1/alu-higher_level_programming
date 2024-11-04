#!/usr/bin/python3


class Rectangle:
    def __init__(self, width = 0, height = 0):
        self._width = width
        self._height = height
    def width(self, value):
        value = self._width
        if value is not int:
            raise TypeError("width must be an integer")
        else if width < 0:
            raise ValueError("width must be an integer")
    def height(self,value):
        value = self._height
        if value is not int:
            raise TypeError("height must be an integer")
        else if value < 0:
            raise ValueError("height must be an integer")
    def area(self):
        return self._height * self._width
    def perimeter(self):
        if width or height == 0:
          return perimeter==0
      else:
          return self._height + self._width 




