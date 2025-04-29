import random

from Point import Point


class PointException(Exception):
    """
    Custom exception for Point-related errors.
    """
    pass


class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with x, y coordinates and a color.

        :param x: The x-coordinate (int or float).
        :param y: The y-coordinate (int or float).
        :param color: A string representing the color.
        """
        # Raise an exception if x or y are not numeric types
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y)  # Call the Point constructor to set x and y
        self.color = color  # Set the color attribute

    def __str__(self):
        """
        Return a formatted string showing color and coordinates.
        """
        return f"<{self.color}: {self.x}, {self.y}>"


# Example usage:
p = ColorPoint(1, 2, "red")  # create a ColorPoint with red color
p.color = "rojo"  # update color
p.x = 200  # change x coordinate

print(p.distance_orig())  # calculate distance from origin
print(p)

# The following block is commented out due to syntax errors and being incomplete
# colors = ["pink, "red", "green", "blue", "yellow", "magenta", "cyan""]
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10,10),
#                    random.choice(colors)))

# print(color_points)
# color_points.sort()
# print(color_points)