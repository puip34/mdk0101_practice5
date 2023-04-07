import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

    def perimeter(self):
        pass

    def move(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def move(self, x, y):
        super().move(x, y)
