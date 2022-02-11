from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area_calc(self):
        pass

    @abstractmethod
    def perimeter_calc(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area_calc(self):
        return self.width * self.length

    def perimeter_calc(self):
        return (self.width + self.length) * 2

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area_calc(self):
        return f"{pi * (self.radius ** 2):.2f}"

    def perimeter_calc(self):
        return f"{(2 * pi * self.radius):.2f}"

    circumference_calc = lambda self: self.perimeter_calc()

class Triangle(Shape):

    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        
    def area_calc(self):
        return (self.base * self.height) / 2

    def perimeter_calc(self):
        return self.base + self.side1 + self.side2

#Example usage
rect = Rectangle(3, 4)
circ = Circle(5)
tri = Triangle(21, 9, 22, 14)

print("Rectangle area:", rect.area_calc())
print("Rectangle perimeter:", rect.perimeter_calc())

print("Circle area:", circ.area_calc())
print("Circle circumference:", circ.circumference_calc())

print("Triangle area:", tri.area_calc())
print("Triangle perimeter:", tri.perimeter_calc())