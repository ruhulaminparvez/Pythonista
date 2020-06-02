"""Python Program for factorial of a number"""

num = int(input("enter a integer: "))

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1) #one line to find factorial

print("Factorial of {0} is".format(num),factorial(num))