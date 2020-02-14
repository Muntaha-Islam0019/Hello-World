# Every class has a constructor, weather you modify it or not. It's
# a function called __init__ (short form of initiation). Also,
# every function in class should have a 'self' parameter.
import math


# noinspection PyMethodMayBeStatic
class Point:

    # class variable
    some_int = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

    def distance(self, x, y):
        return math.sqrt(math.pow(x - self.x, 2) + math.pow(y - self.y, 2))

    # We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases. It's also used for modifying class variables.
    @classmethod
    def a_class_method(cls, change_var):
        cls.some_int = change_var

    @classmethod
    def another_class_method(cls, some_str):
        a, b = some_str.split('_')
        return cls(a, b)


point_one = Point(19, 47)
point_one.point()
print(point_one.distance(0, 0))
print(point_one.__dict__)

point_two = Point.another_class_method('18_20')
point_two.point()
print(point_one.distance(int(point_two.x), int(point_two.y)))
