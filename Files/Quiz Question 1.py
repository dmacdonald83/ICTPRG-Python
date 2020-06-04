def add_values_to_file(filename, a, b):
    result = str(a + b)
    print("Writing result (" + result + ") to " + filename + "...", end='')
    out_file = open(filename, 'w')
    out_file.write(result + "\r\n")
    out_file.close()
    print("Done!")

number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
add_values_to_file('maths.txt', number_one, number_two)
