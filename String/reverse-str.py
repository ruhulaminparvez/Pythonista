"""Write a Python program to reverse a string"""

s = input("enter a string: ")

def reverse_string(str1):
    return ''.join(reversed(str1))

print("reverse string is: ",reverse_string(s))


