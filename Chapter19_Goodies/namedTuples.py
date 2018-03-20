from collections import namedtuple

# Create a class type on the fly!
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

# access the variables by the name
print(p)
print(p.x)
print(p.y)

#or like tuples
print(p[0])
print(p[1])