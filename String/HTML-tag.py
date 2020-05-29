#Write a Python function to create the HTML string with tags around the word(s).
t = (input("write a HTML tag: "))
w = (input("write the word: "))

def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print("HTML string with tags around the word: ",add_tags(t, w))
