"""Python Program to find sum of array"""

# Python 3 code to find sum 
# of elements in given array 
def _sum(arr,n): 
	
	# return sum using sum 
	# inbuilt sum() function 
	return(sum(arr)) 

arr=[] 
# input values to list 
arr = [12, 3, 4, 15] 

# calculating length of array 
n = len(arr) 

ans = _sum(arr,n) 

# display sum 
print ('Sum of the array is ', ans) 

