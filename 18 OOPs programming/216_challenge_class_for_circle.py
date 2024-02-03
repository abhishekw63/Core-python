import math

class Circle:
    def __init__(self, radius):
        self.rd = radius

    def area(self):   
        return math.pi * pow(self.rd, 2)

    def perimeter(self):
        return 2 * math.pi * self.rd

c1 = Circle(7)
print(f'Area: {c1.area()}')
print(f'Perimeter: {c1.perimeter()}')
