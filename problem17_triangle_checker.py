# 17. Triangle Type Checker: Write a Python program that takes three sides of a triangle 
# as input and determines whether it forms an equilateral, isosceles, or scalene triangle.
def triangle_checker(side1, side2, side3):
    if side1 <=0 or side2<=0 or side3 <=0:
        return "Sides must be positive numbers"
    elif side1 == side2 == side3:
        return "The triangle is equilateral"
    elif side1 == side2 or side2== side3  or side1 == side3:
        return "The triangle is issoceles"
    else:
        return "The triangle is scelene"
print(triangle_checker(4,5,6))
