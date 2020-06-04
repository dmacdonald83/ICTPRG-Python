def number_to_list(number):
    digits = []
    for x in str(number):
        digits.append(int(x))
    return digits

print(number_to_list(2342))
