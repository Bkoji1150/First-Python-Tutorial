"""When working with python data"""
from collections import namedtuple 

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=4)
p2 = Point(x=1, y=3)

print(p1 == p2)