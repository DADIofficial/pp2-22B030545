class Shape:
    def __init__(self):
        self.area = 0

    def printarea(self):
        print(self.area)


class Square(Shape):
    def __init__(self, l):
        self.lenght = l
    def print_area_square(self):
        self.area = self.lenght ** 2
        print(self.area)

class Rectangle(Shape):
    def __init__(self, l, w):
        self.lenght = l
        self.width = w
    def print_area_rectangle(self):
        self.area = self.lenght * self.width
        print(self.area)
s = Rectangle(int(input()), int(input()))
s.print_area_rectangle()