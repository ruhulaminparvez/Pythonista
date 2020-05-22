'''Example to illustrate
the use of else statement
with the while loop'''
n = int(input("Enter a value: "))

counter = 0

while counter <= n:
    print("Inside loop")
    counter = counter + 1
else:
    print("Outside loop")
