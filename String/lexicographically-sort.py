"""Write a Python program to sort a string lexicographically"""

s = (input("enter a line of stirng: "))

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print("lexicographically sort: ", lexicographi_sort(s))



