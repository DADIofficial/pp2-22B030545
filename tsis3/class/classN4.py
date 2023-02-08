class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("x =", self.x, "y =", self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
A = Point(int(input()), int(input()))
B = Point(int(input()), int(input()))
A.show()
B.move(int(input()), int(input()))
print(A.dist(B))