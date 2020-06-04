salary = int(input("Enter your salary: "))
years = int(input("How many years have you been in this job? "))
if salary >= 50000:
    if years >= 3:
        print("Congratulations, you qualify for a loan!")
    else:
        print("Sorry, you have not been in your current job long enough.")
else:
    print("Sorry, your salary is too low.")
