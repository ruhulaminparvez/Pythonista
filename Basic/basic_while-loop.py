# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

n = int(input("Enter a number: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum of numbers are: ", sum)
