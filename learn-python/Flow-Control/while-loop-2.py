"""Conditional While-loop - Odd  Number Between X and Y"""

x = int(input("Enter A Min Number: "))
y = int(input("Enter A Max Number: "))

i=x
if i%2 == 0:
    i = x+1

while(i<=y):
    print("Odd Numbers Are:",i)
    i += 2
    
    

