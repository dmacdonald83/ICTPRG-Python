# Import `datetime` module because we'll be needing to get the current year
import datetime

#############################
# ICTPRG407 - Challenge 1
# Teacher: Verghese George (vgeorge@swin.edu.au)
# Student Name: Duncan Macdonald (duncanmac83@gmail.com)
# Student ID: 102827175
# Date: 14/05/2020
#
# Dod&Gy Evil Inc proudly presents, The Huawow Employee Email Cracker!
#
# Program Functionality...
# This program will take input from the user in the form of:
# - employee's first name
# - employee's last name
# - employee's age
# It will then generate a email address and default password from the given information.
# This will repeat until the user input is blank for the employee's first name.
#############################


# Convert the employee's age which happens to magically be offset
# by the third-to-last digit of my Student ID.
# Inputs: 
# - age (integer) ... The raw age of the employee in years
# - student_id (integer) ... My Student ID
# Returns an integer of the age offset by the third-last digit of student_id
def convert_age(age, student_id):
    str_id = str(student_id)
    len_id = len(str_id)
    return age + int(str_id[len_id - 3:len_id - 2])


# Returns the year-of-birth for a specified `age`
# Inputs: 
# - age (integer) ... The age of the employee
# Returns an integer of the year of birth for the employee's age
def get_year_from_age(age):
    return datetime.datetime.now().year - age


# Generates an employee's email address from their `firstname` and `lastname`
# Inputs: 
# firstname (string) ... Employee's First Name
# lastname (string) ... Employee's Last Name
# Returns a string of the employee's email following the format:
#   <first_letter_of_firstname> + <lastname> + "@huawow.io"
# All lowercase.
def generate_email(firstname, lastname):
    email_user = firstname[0:1] + lastname
    return (email_user + '@huawow.io').lower()


# Generates a formatted password for a given `firstname`, `lastname`, and `age`.
# Inputs:
# - firstname (string) ... Employee's First Name
# - lastname (string) ... Employee's Last Name
# - age (integer) ... Employee's (converted) Age
# Returns a string of the formatted password in the following format:
#   <firstname_lowercase> + <first_letter_lastname_uppercase> + "_" + <year_of_birth>
def generate_password(firstname, lastname, age):
    # Password made up from lowercase firstname, uppercase first letter of lastname.
    password = firstname.lower() + lastname[0:1].upper()
    # Followed by '_' and the year of birth
    password += '_' + str(get_year_from_age(age))
    return password


# Generate an employee's email address and password based on their name, age, and my Student ID.
# Inputs:
# - firstname (string) ... Employee's First Name
# - lastname (string) ... Employee's Last Name
# - age (integer) ... Employee's Age
# - student_id (integer) ... My Student ID
# Returns a string of the following format:
#  <email> + "|" + <password>
def generate(firstname, lastname, age, student_id):
    conv_age = convert_age(age, student_id)
    email = generate_email(firstname, lastname)
    password = generate_password(firstname, lastname, conv_age)
    return email + "|" + password


# Takes input from the user and returns a list containing [firstname,lastname,age]
# Inputs: None.
# Outputs: List of...
# - 0 (string) ... Employee First Name
# - 1 (string) ... Employee Last Name
# - 2 (integer) ... Employee Age
# Returns an empty list if input for First Name is empty.
def get_employee_input():
    data = []
    firstname = input("Enter employee First Name: ")
    if (len(firstname) == 0):
        return data
    lastname = input("Enter employee Last Name: ")
    age = input("Enter employee Age: ")
    data.append(firstname)
    data.append(lastname)
    data.append(int(age))
    return data


# Take input until an empty list is returned...
employee = get_employee_input()
while len(employee) > 0:
    # Call the generate function with the user input and my Student ID...
    result = generate(employee[0], employee[1], employee[2], 102827175)
    # Print the generated email and password combination...
    print(result)
    # Take input from the user again...
    employee = get_employee_input()
