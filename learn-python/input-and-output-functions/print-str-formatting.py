"""Print And String Formatting Actions"""

#format-1
name = "Ruhul"
cgpa = 3.80
print("Name is:",name,"Cgpa is:",cgpa)

#format-2 
"""%s is place holder for string, 
%f is place holder for float, 
%i is place holder for integer"""

print("Name is %s,Cgpa is %.2f"%(name, cgpa))

#format-3
"""Another Place Holder Method"""

print("Name is {},Cgpa is {}".format(name, cgpa))

#format-4
"""Holding Place with numbering"""

print("Name is {0},Cgpa is {1}".format(name, cgpa))