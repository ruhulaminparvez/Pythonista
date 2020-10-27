"""Multiple Return Values"""

def calc(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a,b,c,d

result = calc(10,5)
for i in result: print(i)


