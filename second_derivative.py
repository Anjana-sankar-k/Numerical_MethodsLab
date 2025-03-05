def f(x):
    return x**3 + 2*x**2 - 5*x +7

def cdd(x, h):
    return ((f(x+h) + f(x-h) - 2*f(x))/(h**2))

x = 2
h = 0.1

value = cdd(x, h)

print(f"CDD value of f(x) is: {value}") 