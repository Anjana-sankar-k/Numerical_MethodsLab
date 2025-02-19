import math

def f(x):
    return math.exp(x)

def bdd(x, h):
    return ((f(x) - f(x-h))/h)

x = 1
h = 0.01


value = bdd(x, h)

print(f"BDD value of f(x) is: {value}")