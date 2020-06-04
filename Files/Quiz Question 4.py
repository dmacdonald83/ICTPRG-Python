# Calculate the factorial for a given number `count`
def factorial(count):
    f = 1
    for n in range(1, count + 1):
        f *= n
    return f

# Calculate the factorial for each number from 1 to 10 (inclusive)
results = []
lines = []
for i in range(1, 11):
    result = str(factorial(i))
    results.append(result)
    out = str(i) + ' = '
    for ii in range(1,i+1):
        out += str(ii)
        if ii == i:
            out += " -> " + result
            lines.append(out)
        else:
            out += "x"
       

# Output the results to file
lines = "\n".join(lines)
out_file = open('factorials.txt', 'w')
out_file.write(lines)
out_file.close()
