"""Accessing Local And Global Variables"""

x = 123

def display():
    x = 678
    print(x)
    print(globals()['x'])

print(x)

z = display
z()
z()


