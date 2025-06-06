# 24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
n = int(input("Enter a number: "))
f1 = 0
f2 = 1
print(f"Fibonacci series up to {n} terms: ")
for i in range(n):
    print(f1, end=' ')
    f_next = f1 + f2
    f1 = f2
    f2 = f_next
    