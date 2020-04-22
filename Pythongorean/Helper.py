import math


def hypotenuse(a, b):
    c2 = (a * a + b * b)
    c = math.sqrt(c2)
    print(round(c, 1))
    return c


def leg(h, l):
    l2 = (h * h - (l * l))
    l = math.sqrt(l2)
    print(round(l, 1))
    return l


def SQRT(x, x2):
    x: float = math.sqrt(x2)
    print(round(x, 1))
    return x

