# 13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.
def is_leap_year(year):
    if year%400 == 0:
        return f"{year} is a leap year"
    elif year%100 != 0 and year%4 == 0:
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
print(is_leap_year(2020))