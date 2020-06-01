"""Write a Python program to format a number with a percentage"""

x = float(input("enter a integer value: "))
y = float(input("enter another integer value: "))

print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:.2%}".format(x));
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:.2%}".format(y));


