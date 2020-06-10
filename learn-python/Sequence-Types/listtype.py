"""List Types All Actions"""

#random types of list values
lst = [10,20,30,"ruhul",-10,12.3,3]
#output of the list
print("list is:",lst)

#indexing of list
Indx = lst[4]
print("entered index of list is:",Indx)

#Slicing of list
Slic = lst[2:5]
print("slicing of the list is:",Slic)

#repeatation of the list
rep = lst*3
print("repeatation of the list is:",rep)

#length of the list
leng = len(lst)
print("length of the list is:",leng)

#Adding a new element in list at the end
lst.append(12)
print("adding new element in list:",lst)

#Remove value from the list
lst.remove(20)
print("After remove a value from the list:",lst)

#Inbuild Delete function work with index
del lst[4]
print("After Delete USing Index:",lst)

#insert element at a particular position in the list
lst.insert(4, 44)
print("After Insert element at a particular position: ",lst)


#max and min function to find the max and min value of the list
#print("Maximum value of the list is:",max(lst))
#print("Minimum value of the list is:",min(lst))

#Using sort function sorted the list
#lst.sort()
#print("After Sorting the list:",lst)

#Using sort function reverse sorted the list
#lst.sort(reverse=True)
#print("After Sorting the list:",lst)

#using clear function remove all values from the list
#lst.clear()
#print("After Clear the list:",lst)

