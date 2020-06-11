"""list to bytes and bytearray"""
"""bytes can't perform indexing bytearray can perform indexing,
slicing and repeatation both can't perform"""
 
lst = [10,20,30]
print("entered list is:",lst)
print("type is:",type(lst))

#list to bytes
b = bytes(lst)
print("after convert bytes:",type(b))

#list to bytearray
b1 = bytearray(lst)
print("after convert bytearray:",type(b1))


#indexing in bytearray
b1[1]=23
print("Now bytearray is:",b1)


