#program to find the value is positive, Negative, or Zero
num = float(input("Enter a number:"))

if num>=0: #num is greater than zero or equal to zero
    if num==0: #num is equal to zero
        print("Number is Zero")
    else: #num is not equal to zero
        print("Number is positive")
else: #num is not greater than zero or equal to zero
    print("Number is Negative")
