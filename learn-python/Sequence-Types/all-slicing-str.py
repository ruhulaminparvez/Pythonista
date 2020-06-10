"""Slicing String"""

s = input("enter a string: ")
print("entered string is: ", s)

#Using len function we can find out the length of string
s1 = len(s)
print("length of string is: ", s1)

#Using indexing we can reverse the string
s2 = s[::-1]
print("reverse inputed string: ", s2)

#By Using strip we can remove the spaces in the left or right
s3 = s.strip()
print("after striping: ", s3)

#Using find function we can find the position of the entered string at any place
s4 = s.find(input("find position of char: "),0,len(s))
print("char position in the string is: ", s4)

#Using count function we can count the number of char in the entered string
s5 = s.count(input("count the char of: "))
print("number of char in the string is: ", s5)

#Using replace function we can replace two string
s6 = s.replace(input("the word u wanna replace:"),input("the word u wanna replace with:"))
print("atfer replaceing two word: ", s6)

#Using upper function we can convert the string in uppercase
s7 = s.upper()
print("The Uppercase of string is: ", s7)

#Using lower function we can convert the string in lowercase
s8 = s.lower()
print("The Lowercase of string is: ", s8)

#Using title function we can convert the string in titlename type string
s9 = s.title()
print("The Title type of string is: ", s9)