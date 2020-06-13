"""Input Functions All Actions"""

#User Input Method-1
s = input()
print(s)

#User Input Method-2
"""Input With String Quotes"""
s1 = input("Enter Your Name:")
print("Your Name Is:",s1)

#User Input Method-3
"""Input from user with specific type, User input by default set as string type"""
s2 = int(input("Enter a integer:"))
print("Entered integer is:",s2)

#User Input Method-4
"""Multiple input method"""

lst = [x for x in input("Enter three value seperated by comma:").split(',')]
print(lst)



