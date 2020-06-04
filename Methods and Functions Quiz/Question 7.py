def PrintBoxByWidth(width):
    for y in range(5):
        print('x', end='')
        for x in range(width - 2):
            if y % 2 == 0:
                if y == 2:
                    print('o', end='')
                else:
                    print('x', end='')
            else:
                print(' ', end='')
        print('x', end='')
        print('')

PrintBoxByWidth(60)
