"""Write a Python program to accept a filename from the user and print the extension of that"""

s = input("enter  a filename with extension: ")
file_extn = s.split(".")

print("file extension is: ", repr(file_extn[-1]))
