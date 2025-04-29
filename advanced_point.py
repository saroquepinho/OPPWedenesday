from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint with x, y coordinates and a validated color.
        """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x  # private x attribute
        self._y = y  # private y attribute
        self._color = color  # private color attribute

    @property
    def x(self):
        """
        Getter for x coordinate.
        """
        return self._x  # return x value

    @x.setter
    def x(self, value):
        """
        Setter for x coordinate.
        """
        self._x = value  # set x value

    @property
    def y(self):
        """
        Getter for y coordinate.
        """
        return self._y  # return y value

    @property
    def color(self):
        """
        Getter for color.
        """
        return self._color  # return color value

    @classmethod
    def add_color(cls, color):
        """
        Add a new valid color to the COLORS list.
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create a new AdvancedPoint from a tuple instead of two separate values.
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate distance between two points.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5  # standard distance formula

    def distance_to_other(self, p):
        """
        Calculate distance from self to another AdvancedPoint.
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

# Example usage:
AdvancedPoint.add_color("rojo")  # add new color "rojo"
p = AdvancedPoint(1, 2, "rojo")
print(p.x)
print(p)
print(p.distance_orig())  # distance from origin
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))  # distance between p and p2
print(p.distance_to_other(p2))  # distance between p and p2 using instance method
