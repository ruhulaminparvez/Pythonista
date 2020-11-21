"""Python program to print all Prime numbers in an Interval"""

# Python program to print all  
# prime number in an interval 
  
start = (int(input("start integer: ")))
end = (int(input("end integer: ")))
  
for val in range(start, end + 1): 
    if val > 1: 
        for n in range(2, val//2 + 2): 
            if (val % n) == 0: 
                break
            else: 
                if n == val//2 + 1: 
                    print("prime numbers in the intervals are: ",val) 


