"""Write a Python program to display a number in left, right and center aligned of width 10"""

x = int(input("enter a integer: "))

print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));

