def array_join(list1, list2):
    return list1 + list2

def array_join_algorithm(list1, list2):
    for x in list2:
        list1.append(x)
    return list1

print(array_join([ 'a', 'b', 'c' ], [ 1, 2, 3 ]))
print(array_join_algorithm([ 'a', 'b', 'c' ], [ 1, 2, 3 ]))
