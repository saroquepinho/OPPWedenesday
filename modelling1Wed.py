import random

from point import Point

class ColorPoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
print(p)
colors = ["pink, "red", "green", "blue", "yellow", "magenta", "cyan""]
color_points = []
for i in range(10):
    color_points.append(
        ColorPoint(random.randint(-10,10),
                   random.randint(-10,10),
                   random.choice(colors)))

print(color_points)
color_points.sort()
print(color_points)