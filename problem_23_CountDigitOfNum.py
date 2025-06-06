# 23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.


n = int(input("Enter a number: "))
count = 0
while n > 0:
    digit = n % 10
    count +=1
    n//=10
print(f"Number of digits in the given number is: {count}")
