sTest = str(input("Enter a line of string: "))


if(sTest.count('/') == 2):
    print("This line have a Double Slash") 
    print("Position of double slash",sTest.find("//"),0,len(sTest))

elif(sTest.count('/') == 1):
    print("Single Slash")
    print("positon of single slash",sTest.find("/"),0,len(sTest))
else:
    print('Error: Test string have no slash')
