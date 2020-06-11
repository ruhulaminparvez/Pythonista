"""All Tuple Actions"""
"""Tuple sequnce type just like a list but it's Can't Modified.
For this reason we can't use append(),extend(),insert(),remove(),clear()"""

#empty tuple
tple = ()
print(tple)

#value in tuple
tpl = (10,20,23,12,"Ruhul")
print("entered tuple is:",tpl)

#index value in tuple 
inx = tpl[3]
print("Index value is:",inx)

#Repeatations
rep = tpl*3
print("Repeatation of tuple is:",rep)

#Count in tuple
print("Count a value in tuple:",tpl.count(23))

#Index number find in tuple
print("Index number of tuple is:",tpl.index(23)) 

