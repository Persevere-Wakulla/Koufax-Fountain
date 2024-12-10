import math

def distance(p1, p2):
    a = p1.x - p2.x
    b = p1.y - p2.y
    c = math.hypot(a, b)
    return c