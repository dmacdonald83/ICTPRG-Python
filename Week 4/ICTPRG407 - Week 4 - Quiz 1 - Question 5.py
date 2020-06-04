print("Enter some numbers (Press x to stop):")
sum = 0
num = input()
while num != 'x':
    sum += int(num)
    num = input()
print("Total: ", sum)
