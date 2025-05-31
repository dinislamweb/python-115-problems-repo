#7. String Palindrome: Write a Python function to check if a given string is a palindrome or not.
def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
print(is_palindrome("madam"))
