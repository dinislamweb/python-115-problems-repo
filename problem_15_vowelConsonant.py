# 15. Vowel or Consonant: Write a Python program that takes a single character 
# as input and determines whether it is a vowel or a consonant.
def is_vowel_or_consonant(char):
    vowels = 'aeiouAEIOU'
    if len(char) != 1 or not char.isalpha():
        return "Please enter a single aplhbetical character"
    if char in vowels:
        return f"{char} is a vowel"
    else:
        return f"{char} is a consonant"
print(is_vowel_or_consonant('a'))