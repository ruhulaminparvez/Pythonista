"""Question 1: Given a two integer numbers return their product and  
if the product is greater than 1000, then return their sum"""

def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

number1 = int(input("Enter 1st Integer: ")
number2 = int(input("Enter 2nd Integer: ")

print("\n")
result = multiplication_or_sum(number1, number2)
print("The result is", result)

"""Question 2: Given a range of first 10 numbers, Iterate from start number 
to the end number and print the sum of the current number and previous number"""

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)


