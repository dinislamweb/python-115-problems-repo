#9. String Concatenation: Write a Python program that takes two strings as input 
# and concatenates them into a single string without using the `+` operator.
def concatenate_strings(str1, str2):
    """string concatenation without using the + operator
       Args:
       str1(str):first string
       str2(str):second string
    """
    #result = " ".join([str1, str2])
    result = str1.concate(str2)
    return result
print(concatenate_strings("hello", "Din Islam"))