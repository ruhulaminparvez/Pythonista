"""Write a Python program to display the current date and time."""

import datetime

now = datetime.datetime.now()
print("current Date and Time is:",now.strftime("%Y-%m-%d %H:%M:%S"))
