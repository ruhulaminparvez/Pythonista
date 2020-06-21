"""Multiple Conditions - Handle Zero"""

x = int(input("Enter A Integer: "))

if x == 0:
    print(x,"Is Zero")
elif x%2 == 0:
    print(x,"Is Even Number")
else:
    print(x,"Is Odd Number")