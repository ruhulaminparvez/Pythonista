 #Write a Python program to remove the nth index character from a nonempty string.

str = (str(input("enter a string: ")))
n = (int(input("which nth index u wanna remove: ")))

def remove_char(str, n):
      first_part = str[:n]
      last_part = str[n+1:]
      return first_part + last_part
print("After Delete: ",remove_char(str , n))
