# 18. Quadratic Equation Solver: Write a Python program that takes 
# the coefficients (a, b, c) of a quadratic equation as input and calculates
# and prints the real roots (if they exist) or a message indicating the complex roots.
import cmath
def quadratic_solver(a,b,c):
    if a == 0:
        return "Coefficient 'a' cannot be zero in a quadratic equation."
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b  -cmath.sqrt(discriminant))/ (2*a)
        return f"The root are real and different: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"The root is real and same: {root}"
    else:
        real_part = -b /(2*a)
        imaginary_part = cmath.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return f"The roots are complex: {root1} and {root2}"
a = float(input("Enter coefficienta : "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
print(quadratic_solver(a,b,c))
        