values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45, 78]

def sum_list (values):
    sum = 0
    for x in values:
        sum = sum + x
    return sum

def average_list (values):
    return int(sum_list(values) / len(values))

def max_list (values):
    max = values[0]
    for x in values:
        if x > max:
            max = x
    return max


print("Sum of List:", sum_list(values))
print("Average of List:", average_list(values))
print("Max in List:", max_list(values))
