"""Write a python program to count repeated characters in a string."""

import collections
str1 = input("enter a line of string: ")
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))

