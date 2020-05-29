'''Write a Python function to get a string made of 4 copies of the
last two characters of a specified string (length must be at least 2).'''

s = (input("enter a string: "))

def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print("last two char copies: ", insert_end(s))
