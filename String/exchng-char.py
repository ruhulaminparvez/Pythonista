# Write a Python program to change a given string to
##a new string where the first and last chars have been exchanged

str1 = (str(input("enter a string: ")))

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]

print("after exchanged: ",change_sring(str1))
