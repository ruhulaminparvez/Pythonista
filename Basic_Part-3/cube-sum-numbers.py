"""Python Program for cube sum of first n natural numbers"""

# Simple Python program to find sum of series 
# with cubes of first n natural numbers 
n = int(input("enter a natural number: "))
  
# Returns the sum of series  
def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum
  
print("output: ",sumOfSeries(n))


