"""Question 3: Given a string, display only those 
characters which are present at an even index number."""

def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "pynative" 
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)


"""Question 4: Given a string and an integer number n, 
remove characters from a string starting from zero up to n and return a new string"""

def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 4))