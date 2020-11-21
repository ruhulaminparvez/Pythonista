"""Function Inside Another"""

x = str(input("Enter A String: "))

def display(name):
    def message():
        return "Hello "
    result = message()+name
    return result

print(display(x))