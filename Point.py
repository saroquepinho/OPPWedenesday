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



# now we need to instantiate it!
p = Point(1,2) # p is an instance of 1 and 2
p2 = Point(2,3)
p4 = Point(4.4, -55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
print(f"the point x is equal to", p.x)
print(p)