"""Set to FrozenSet"""
"""Frozen set even not support update() or remove()"""

s = {10,20,30,40}
print("The set is:",s)
print("Type is:",type(s))

#convert set to frozenset
f = frozenset(s)
print("The frozen set is:",f)
print("Type Now:",type(f))


