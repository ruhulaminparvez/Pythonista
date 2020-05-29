#Write a Python function to reverses a string if it's length is a multiple of 4.

s = (input("enter a string: "))

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return "no change!!",str1

print("reverse string is: ",reverse_string(s))
