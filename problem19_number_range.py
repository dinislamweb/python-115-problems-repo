# 19. Number Ranges: Write a Python program that takes an integer as input and prints whether 
# the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.
def number_range(num):
    if num >=0 and num <= 50:
        return f"{num } is the range of 0-50"
    elif num >= 51 and num <=100:
        return f"{num} is the range of 51-100"
    elif num >= 101 and num <=150:
        return f"{num} is the range of 101-150"
    elif num > 150:
        return f"{num} is above 150"
    else:
        return "Please enter a valid number"
num  = int(input("Enter a numbe: "))
print(number_range(num))

