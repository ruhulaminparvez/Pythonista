#list
item1 = [1, 3.2, 'omi']
item3 = [2, 6.7, 'nafi']

#check the type
print(type(item1))

#indexing item2
print(item1[2])

#add value at the last position of the list
item1.append(5)
print(item1)

#insert value at a specified position of the list
item1.insert(0, 'aloe')
print(item1)

#add value at the last position of the list
item1.append(-3/6)
print(item1)

#add elements from another list to the current list
item1.extend(item3)
print(item1)

#tuple
item2 = (1, 2.3, 'nafiza')

#check type of data
print(type(item2))

#indexing fo item2
print(item2[2])