"""Python Program for compound interest"""

#Compound Interest = P(1 + R/100)**t
#P is principle amount
#R is the rate and
#T is the time span

p = (float(input("enter principle amount: ")))
r = (float(input("enter the rate: ")))
t = (float(input("enter the time: ")))

ci = p * (pow((1 + r / 100), t))

print("compound interest is: %.2f"%ci)