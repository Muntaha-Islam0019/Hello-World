# Every class has a constructor, weather you modify it or not. It's
# a function called __init__ (short form of initiation). Also,
# every function in class should have a 'self' parameter.
import math


# noinspection PyMethodMayBeStatic
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

    def distance(self, x, y):
        return math.sqrt(math.pow(x - self.x, 2) + math.pow(y - self.y, 2))


pointOne = Point(19, 47)
pointOne.point()
print(pointOne.distance(0, 0))
