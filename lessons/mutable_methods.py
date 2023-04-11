from __future__ import annotations

class Point:
    """Model a 2D Point"""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with its x, y components"""
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __str__(self):
        """Print prettier version of our point"""
        return f"({self.x}, {self.y})"
        # returns (1.0, 2.0) when calling print(str(a))

    # overloaded operation - overloard multiplication
    def __mul__(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    # overload
    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a.scale(3.0)

print(type(1))
print(type(str(1)))
print(str(a))
# print(a) - gives same as print(str)
print(b) # prints like str was called
print(f"My point is: {b}")
c: Point = a * 3.0 # made mul to explain Point and float multiplication
print(c)
print(c[1]) # y-coordinate