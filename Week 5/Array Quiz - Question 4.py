
fullname = input("Enter your Full Name: ")
words = fullname.split()
initials = []
for word in words:
    initials.append(word[0])
print("Full Name:", fullname)
print("Initials:", ''.join(initials).upper())
