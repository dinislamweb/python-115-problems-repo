# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) 
# as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.
def time_message(hour):
    if 0 <=hour < 12:
        return "Good Morning"
    elif 12 <=hour <17:
        return "Good Afternoon"
    elif 17 <=hour <21:
        return "Good Evening"
    elif 21 <= hour < 24:
        return "Good Night"
    else:
        return "Invalid hour. Please enter a valid hour (0 - 23)"
hour = int(input("Enter the hour: ")) 
print(time_message(hour))