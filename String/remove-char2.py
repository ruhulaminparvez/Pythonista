 #Write a Python program to remove the characters which have odd index values of a given string.

s = (str(input("enter a string: ")))

def odd_values_string(str1):
  result = ""
  for i in range(len(str1)):
    if i % 2 == 0:
      result = result + str1[i]
  return result

print("after delete odd values: ",odd_values_string(s))
