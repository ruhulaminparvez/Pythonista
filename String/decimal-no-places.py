"""Write a Python program to print the following floating numbers with no decimal places."""

x = float(input("Enter float number: "))
y = float(input("Enter another float number: "))
print("\nOriginal Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x));
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y));

