"""
homework 22
"""
import math

class Square:
    """_summary_
    """
    def __init__(self, side):
        """_summary_

        Args:
            side (_type_): _description_
        """
        self.side = side
    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.side ** 2
    def perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return 4 * self.side
class Circle:
    """_summary_
    """
    def __init__(self, radius):
        """_summary_

        Args:
            radius (_type_): _description_
        """
        self.radius = radius
    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return math.pi * self.radius ** 2
    def circumference(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return 2 * math.pi * self.radius
class CircleInSquare(Square, Circle):
    """_summary_

    Args:
        Square (_type_): _description_
        Circle (_type_): _description_
    """
    def __init__(self, side):
        """_summary_

        Args:
            side (_type_): _description_
        """
        super().__init__(side)
        self.radius = self.side / 2
    def circle_area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().area()
    def square_area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().area()
    def circle_circumference(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().circumference()
    def square_perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().perimeter()

if __name__ == "__main__":
    square = CircleInSquare(7)
    print("Square side:", square.side)
    print("Square area:", square.square_area())
    print("Square perimeter:", square.square_perimeter())
    print("Circle radius (inscribed in square):", square.radius)
    print("Circle area (inscribed in square):", square.circle_area())
    print("Circle circumference (inscribed in square):", square.circle_circumference())
