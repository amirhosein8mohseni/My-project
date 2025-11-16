import math


def a1(x):
    # y = √(sin(x) + 1)
    return math.sqrt(math.sin(x) + 1)


def b2(x):
    # y = √(sin(x) / cos(x)) 
    return math.sqrt(math.sin(x) / math.cos(x))


def c3(x):
    # y = √(tan(x) / sin(x)) 
    return math.sqrt(math.tan(x) / math.sin(x))


def e4(x,e):
    # y = √(1 / (1 + e**(-x))) 
    return math.sqrt(1 / (1 + e**(-x)))


def f5(w,a):
    # y = w - a * (√w / √a)
    return w - a * (math.sqrt(w) / math.sqrt(a))


def g6(x,e):
    # y = 1 - e**sin(x) 
    return 1 - e**(math.sin(x))


print(a1(10))
print(b2(9))
print(c3(8))
print(e4(7,7))
print(f5(6,6))
print(g6(5,5))