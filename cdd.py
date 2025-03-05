import math
def f(x):
    return math.sin(x)

def cdd(x, h):
    return ((f(x+h) - f(x-h))/(2*h))

x = math.pi/4
h = 0.05

value = cdd(x, h)

print(f"CDD value of f(x) is: {value}") 