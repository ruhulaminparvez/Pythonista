""" Write a Python program to print the following floating numbers upto 2 decimal places with a sign """

x = (float(input("input a float value: ")))
y = (float(input("input another float value: ")))
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y));

