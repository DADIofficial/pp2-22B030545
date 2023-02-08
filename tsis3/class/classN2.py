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

s = Square(int(input()))
s.print_area_square()