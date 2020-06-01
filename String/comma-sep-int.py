"""Write a Python program to display a number with a comma separator"""

x = int(input("enter a integer value: "))
y = int(input("enter another integer value: "))
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x));
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y));


