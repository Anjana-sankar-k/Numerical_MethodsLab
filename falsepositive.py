import sympy as sp

def bisection_method(equation, a, b, max_iter):
    x = sp.symbols('x')
    f = sp.sympify(equation)
    
    if f.subs(x,a)*f.subs(x,b) > 0:
        print("the function must have opposite signs for a and b")
        
    print(f"Equation: {equation}")
    print(f"initial interval: [{a},{b}]")
    
    for iteration in range(1, max_iter + 1):
        c = (a*f(b) - b*f(a)/f(b) - f(a))
        fc = f.subs(x,c)
        
        print(f"iteration{iteration}: c = {c}, f(c) = {fc}")
        
        if abs(fc) < 0.000001 or (b - a)/2 < 0.000001:
            print(f"root found: {c}")
            return c
        
        if f.subs(x,a)*fc < 0:
            b = c
        else:
            a = c
        
        print("Maximum iterations reached. Approximation may not be accurate. ")
        return (a*f(b) - b*f(a)/f(b) - f(a))
    
equation = input("Enter equation in terms of x: ")
a = float(input("Enter lower bound of interval (a): "))
b = float(input("Enter upper bound of interval (b): "))
max_iter = int(input("Enter maximum number of iterations"))

root = bisection_method(equation, a, b, max_iter)
if root is not None: 
    print(f"Approximate root: {root}")