#1. Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.
a = 10
b = 20
a =  a + b
b = a - b
a = a - b
print(f"After swapping: \na = {a}\nb = {b}")
