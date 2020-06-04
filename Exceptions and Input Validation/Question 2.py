# Write a function called 'InputNumber' that will keep asking the user 
# to enter a value until the value is a valid number, then return it.
def InputNumber():
    num = input("Enter a number: ")
    while not num.isnumeric():
        num = input("Enter a number: ")
    return int(num)
    
print("Finally a valid number: " + InputNumber())
