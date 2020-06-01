"""Write a Python program to strip a set of characters from a string"""

s = input("enter a line of string: ")
s1 = set(input("strippng of set are: "))

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

print("\nOriginal String: ",s)
print("stripping chars: ",s1)      
print("after stripping: ",strip_chars(s , s1))


