def get_largest(list):
    return max(list)

def get_largest_algorithm(list):
    max_number = list[0]
    for x in list:
        if x > max_number:
            max_number = x
    return max_number

print(get_largest([ 4, 3, 7, 2, 4, 9, 1 ]))
print(get_largest_algorithm([ 4, 3, 7, 2, 4, 9, 1 ]))
