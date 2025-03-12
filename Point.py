import random

class Point:
    def __init__(self, x, y):
        """
        Initiate a Point Project
        :param x: the x position
        :param y: the y position
        """
        self.x = x # define x attribute via self.x
        self.y = y # and assign value x to it

    def __str__(self):
        """
        Magic Method that is called when we try to print an instance
        :return: <x,y>
        """
        return f"<x={self.x},y={self.y}>"

    def __repr__(self):
        return self.__str__() # use the same way of printing as str

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5 # square root of the sum x and y squared

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

# now we need to instantiate it!

p = Point(1,2) # p is an instance of 1 and 2
p2 = Point(2,3)
p4 = Point(4.4, -55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
print(f"the point x is equal to", p.x)
print(p)

#create a list of 5 random points

points = []
for i in range(5):
    points.append(Point(random.randint(-10,10), # x value
                        random.randint(-10, 10))) # y value
print("I got these 5 random points:")
print(points)
p = Point(3,4)
print(p.distance_orig()) # except 5 answer
p2 = Point(1,1)
print(f"I am comparing p > p2: {p>p2}") # I expect to have True
print("the sorted list of point is:")
points.sort()
print(points)