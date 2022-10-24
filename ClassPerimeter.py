import math

class Rectangle:
    def __init__(self, lenght, width):
        self.rectangle_length = lenght
        self.rectangle_width = width

    def get_perimeter(self):
        return 2 * (self.rectangle_length + self.rectangle_width)


class Square:
    def __init__(self, side):
        self.square_side = side

    def get_perimeter(self):
        return self.square_side * 4





class Circle():
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
