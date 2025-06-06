# 21. Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    if i == 0 or i == 1:
        fact = 1
    else:
        fact *=i
print(f"Factorial of {i} is {fact}")