"""Write a Python program which accepts a sequence of comma-separated
numbers from user and generate a list and a tuple with those numbers"""

values = input("input some comma seprated integers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
