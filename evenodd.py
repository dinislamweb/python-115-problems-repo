#2. Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
