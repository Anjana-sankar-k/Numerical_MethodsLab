def f(x):
    return x**3 + 2*x**2 - 5*x +7

def fdd(x, h):
    return ((f(x+h) - f(x))/h)

x = 2
h = 0.1


value = fdd(x, h)

print(f"FDD value of f(x) is: {value}")