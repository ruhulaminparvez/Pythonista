#python program to illustrate function with main
def getInteger():
    result = int(input("Enter Integer: "))
    return result

def Main():
    print("Started")

    #calling the getInteger function and store its returned value in the output value
    output = getInteger()
    print(output)

#for Main function existance
if __name__ =="__main__":
    Main()