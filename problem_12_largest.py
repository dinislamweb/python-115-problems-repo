# 12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.
def largest_of_three(num1,num2,num3):
    if num1>num2 and num1>num3:
        return f"{num1} is the largest number"
    elif num2>num3:
        return f"{num2} is the largest number"
    else:
        return f"{num3} is the largest number"
print(largest_of_three(10,50,30))