import re

date_message = "Enter the date in dd/mm/yyyy format: "
date_input = input(date_message)
while not re.search("^[0-9]{1,2}/[0-9]{1,2}/[0-9]{1,4}$", date_input):
    print("Invalid date format!")
    date_input = input(date_message)

date_parts = date_input.split('/')
print("Day:", date_parts[0])
print("Month:", date_parts[1])
print("Year:", date_parts[2])
