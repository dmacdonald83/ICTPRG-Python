num = input("Enter a large number: ")
sum = 0
addition = ''
for ch in num:
    sum = sum + int(ch)
    addition = addition + ' + ' + ch
print("Sum of the digits:", addition[3:], "=", sum)
