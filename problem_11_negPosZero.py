# 11. Positive, Negative, or Zero: Write a Python program that 
# takes a number as input and prints whether it is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "Postive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(10))