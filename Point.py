import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point with x and y coordinates.
        """
        self.x = x  # set x position
        self.y = y  # set y position

    def __str__(self):
        """
        Format the point for printing.
        """
        return f"<x={self.x},y={self.y}>"

    def __repr__(self):
        """
        Use the same format as __str__ when representing.
        """
        return self.__str__()  # same as __str__

    def distance_orig(self):
        """
        Compute distance from origin.
        """
        return (self.x**2 + self.y**2)**0.5  # √(x² + y²)

    def __gt__(self, other):
        """
        Compare points by distance from origin (greater than).
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Compare points by distance from origin (equality).
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance  # note: this uses > not ==

# now we need to instantiate it!

p = Point(1, 2)  # p is an instance of 1 and 2
p2 = Point(2, 3)
p4 = Point(4.4, -55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
print(f"the point x is equal to", p.x)
print(p)

# create a list of 5 random points

points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10),  # x value
                        random.randint(-10, 10)))  # y value
print("I got these 5 random points:")
print(points)

p = Point(3, 4)
print(p.distance_orig())  # expect 5
p2 = Point(1, 1)
print(f"I am comparing p > p2: {p > p2}")  # I expect to have True
print("the sorted list of point is:")
points.sort()
print(points)

