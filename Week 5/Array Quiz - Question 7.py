numbers = []
num = input("Enter a number: ")
while num != 'x':
    numbers.append(int(num))
    num = input("Enter a number: ")
numbers.sort()
duplicates = []
last = -123456789
for x in numbers:
    if x == last and x not in duplicates:
        duplicates.append(x)
    last = x
print("Repeating Numbers:", duplicates)
