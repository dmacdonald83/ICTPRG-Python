for x in range(0, 5):
    for y in range(0, 5):
        print('x', end='')
    print('')

#Bonus points? Here's an Alternative Method:
print("Alternative method:")
for x in range(0, 25):
    if x % 5 == 4:
        print('x')
    else:
        print('x', end='')
