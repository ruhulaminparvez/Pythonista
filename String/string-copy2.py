'''Write a Python function to get a string made of its first three characters
of a specified string. If the length of the string is less than 3 then return
the original string. Go to the editor Sample function and result'''

s = (input("enter a stirng: "))

def first_three(str):
	return str[:3] if len(str) > 3 else str

print("Output :",first_three(s))
