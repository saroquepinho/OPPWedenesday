import random

from Point import Point
import random

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        # raise an exception if we try to have not a number
        if not isinstance(x, (int,float)):
            raise TypeError("x must be an number")
        if not isinstance(y, (int,float)):
            raise TypeError("y must be an number")

        super().__init__(x, y) # this replaces self.x and self.y that can be found on Point.py
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
p.color = "rojo"
p.x = 200

print(p.distance_orig())
print(p)
#colors = ["pink, "red", "green", "blue", "yellow", "magenta", "cyan""]
#color_points = []
#for i in range(10):
#    color_points.append(
 #       ColorPoint(random.randint(-10,10),
  ##                random.choice(colors)))

#print(color_points)
#color_points.sort()
#print(color_points)