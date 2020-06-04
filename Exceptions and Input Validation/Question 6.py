def GetEmailAddress():
    isValid = False
    while not isValid:
        email = input("Enter email address: ")
        parts = email.split('@')
        isValidParts = len(parts) == 2
        if isValidParts:
            isValidLength = len(parts[0]) > 2 and len(parts[0]) <= 32 and len(parts[1]) > 2 and len(parts[1]) <= 32
            isValidDot = parts[1].find(".") >= 0
            isValid = isValidLength and isValidDot
    print(email)

GetEmailAddress()
