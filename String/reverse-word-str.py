"""Write a Python program to reverse words in a string"""

s = input("enter a line of string: ")

def reverse_string_word(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))

print("reverse words of string: ",reverse_string_word(s))


