from ClassPerimeter import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 6)

print(rect_1.get_perimeter())
print(rect_2.get_perimeter())

square_1 = Square(5)
square_2 = Square(7)

print(square_1.get_perimeter())
print(square_2.get_perimeter())

circle_1 = Circle(5)
circle_2 = Circle(10)

print(circle_1.perimeter())
print(circle_2.perimeter())