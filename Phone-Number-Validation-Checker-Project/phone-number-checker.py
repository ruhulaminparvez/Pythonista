import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNumber = input("Enter Mobile Number with Country Code: ")
mobileNumber = phonenumbers.parse(mobileNumber)

#get timezone a phone number
print(timezone.time_zones_for_number(mobileNumber))

#getting carrier of a phone number
print(carrier.name_for_number(mobileNumber, "en"))

#getting region information
print(geocoder.description_for_number(mobileNumber, "en"))

#validating a phone number
print("Valid Mobile Number: ", phonenumbers.is_valid_number(mobileNumber))

#checking possibility of a number
print("Checking Possibility Of Number: ",phonenumbers.is_possible_number(mobileNumber))
