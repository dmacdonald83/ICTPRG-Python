import math

def task1():
  a = float(input("Enter first value: "))
  b = float(input("Enter second value: "))
  if (a == 0 or b == 0):
      print("Error: values cannot be zero")
      return
  print("Multiplied:", a * b)
  print("Summed:", a + b)
  print("Subtracted:", a - b)
  divided = a / b
  print("Divided:", divided)
  if ((a > b and a % b != 0) or (b > a and b % a != 0)):
    print("Remainder? Yes")
  else:
    print("Remainder? No")


task1()

