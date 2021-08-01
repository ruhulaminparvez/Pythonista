print(' Calculator ')
first=float(input('Enter your 1st value:'))
second=float(input('Enter your 2nd value:'))

sum=first+second
sub=first-second
multipy=first*second
divied=first/second

remainder=first%second
power=first**second

print(f'{first}+{second}= ',sum)
print(f'{first}-{second}= ',sub)
print(f'{first}*{second}=',multipy)
print(f'{first}/{second}=', divied,f'remainder =',remainder)
print(f'{first}**{second}',power)
print(f'round=',round(first))
print(f'abstract=',abs(first))
