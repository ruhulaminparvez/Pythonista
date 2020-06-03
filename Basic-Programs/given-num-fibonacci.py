"""Python Program for How to check if a given number is Fibonacci number?"""

x = int(input("where to start check fibonacci number? "))
y = int(input("where u end check fibonacci number? "))

# python program to check if x is a perfect square 
import math 

# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
	s = int(math.sqrt(x)) 
	return s*s == x 

# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 

	# n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
	# is a perferct square 
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
	
# A utility function to test above functions 
for i in range(x,y): 
	if (isFibonacci(i) == True): 
		print (i,"is a Fibonacci Number")
	else: 
		print (i,"is a not Fibonacci Number")
