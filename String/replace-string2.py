'''Write a Python program to find the first appearance
of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string'''

s = (str(input("Write a line of string: ")))

def not_poor(str1):
  snot = str1.find('not') #find 'not' and 'find' on given string line
  spoor = str1.find('poor')


  if spoor > snot and snot>0 and spoor>0:  #if not follows the poor
    str1 = str1.replace(str1[snot:(spoor+4)], 'good') #'not' remove and 'poor' replace with 'good'
    return str1
  else:
    return str1 #if 'not' and 'poor' not on given string then return as it is

print("Output Is: ",not_poor(s))
