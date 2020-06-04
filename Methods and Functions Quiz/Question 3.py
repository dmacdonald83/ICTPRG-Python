def FibonacciAdder(n):
    f1 = 0
    f2 = 1
    sum = 0
    for i in range(n - 1):
        sum = sum + f2
        fnext = f1 + f2
        f1 = f2
        f2 = fnext
    return sum

print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))