def print_chars(num, ch):
    for col in range(num):
        print(ch, end='')
    print('')

for row in range(10):
    print_chars(15, '*')
