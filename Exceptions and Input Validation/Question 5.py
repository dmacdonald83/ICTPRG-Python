def GetPassword():
    isValid = False
    while not isValid:
        pass1 = input("Enter Password: ")
        pass2 = input("Confirm Password: ")
        isValid = pass1 == pass2 and len(pass1) >= 7 and pass1.find("password") == -1
        if isValid:
            hasLowerChar = hasUpperChar = hasNumber = hasSymbol = False
            for ch in pass1:
                if ch.islower():
                    hasLowerChar = True
                if ch.isupper():
                    hasUpperChar = True
                if ch.isdigit():
                    hasNumber = True
                if not ch.isalpha() and not ch.isdigit():
                    hasSymbol = True

            isValid = hasLowerChar and hasUpperChar and hasNumber and hasSymbol

    print("valid password")
    return pass1


GetPassword()
