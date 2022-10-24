import math

class Rectangle:
    def __init__(self, lenght, width):
        self.rectangle_length = lenght
        self.rectangle_width = width

    def get_area(self):
        return self.rectangle_length * self.rectangle_width


class Square:
    def __init__(self, side):
        self.square_side = side

    def get_area_square(self):
        return self.square_side ** 2




class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        return math.pi * self.radius ** 2
