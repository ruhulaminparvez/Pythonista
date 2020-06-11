"""All sets actions"""
"""set does not support indexing,slicing,repeatation"""

s = {10,20,30,40,"ruhul",-10,2.34}
print("The set is:",s)
print("Type is:",type(s))

#set doesn't allows duplicates
s1 = {10,20,30,"ruhul",10,20,30,"ruhul"}
print("Output is:",s1)


#to perform update the set we can use update()
s.update([50,60])
print("After Update the set:",s)

#to remove value from set we can use remove()
s.remove(20)
print("After remove one value set is:",s)
