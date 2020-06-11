"""Dictionary/Map all actions"""

dict1 = {1:"ruhul",2:"amin",3:"parvez"}
print("entered dictionary values:",dict1)

#using item() we can find all the item in the map
print("Items in the map:",dict1.items())

#we can find key numbers in map using its key()
k = dict1.keys()
for i in k:
    print("keys of given map:",i)
    
#we can find value under the keys through its values()
v = dict1.values()
for i in v:
    print("Values of given map:",i)

#we can remove keys or values using python default function del
del dict1[3]
print("after delete a value:",dict1)

