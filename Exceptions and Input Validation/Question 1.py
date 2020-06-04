# Write a program called 'InputNumber' that will keep asking the user 
# to enter a value until the value is a valid number, then print it.
num = input("Enter a number: ")
while not num.isnumeric():
    print("Invalid number!")
    num = input("Enter a number: ")
print("Finally a valid number: " + num)
