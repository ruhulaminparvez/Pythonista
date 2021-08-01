a=int(input('first side value: '))
b=int(input('second side value: '))
c=int(input('third side value: '))

s=(a+b+c)/2
print(f'semi-perimetre: ',s)

#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print('Area: ',area)