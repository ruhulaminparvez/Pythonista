#Write a Python function to insert a string in the middle of a empty bracets.

s = (input("insert a bracet: "))#example: {{}}
w = (input("enter a string: "))

def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print("after insert in the middle: ",insert_sting_middle(s,w))
