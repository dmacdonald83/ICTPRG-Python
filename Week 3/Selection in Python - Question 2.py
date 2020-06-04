sum = int(input("Enter score 1: "))
sum += int(input("Enter score 2: "))
sum += int(input("Enter score 3: "))
average = sum / 3
print("Average score is " + str(average))
if average > 90:
    print("Congratulations!")
