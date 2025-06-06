# 25. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.

n = int(input("Enter a number: "))
sumOfEven  = 0
for i in range(2, n+1,2):
    sumOfEven += i
print(f"Sum of even number from 1 to {n} is {sumOfEven}")
