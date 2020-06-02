"""Python Program for simple interest"""

# Python3 program to find simple interest 
# for given principal amount, time and 
# rate of interest.

p = (int(input("enter principle amount: ")))
r = (int(input("enter the rate: ")))
t = (int(input("enter the time: ")))

si = (p * t * r)/100

print("simple interest is: ",si)    
