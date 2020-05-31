'''Write a Python function to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters.'''

s = (input("enter a string: "))

def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print("output: ", to_uppercase(s))


