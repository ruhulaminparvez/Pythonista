s = (str(input("Write a line of stirng: ")))

def string_both_ends(str):
  if len(str) < 2:
    return''

  return str[0:2] + str[-2:]

print("Output: ", string_both_ends(s))
s = (str(input("Write a line of stirng: ")))
print("Output: ", string_both_ends(s))
