users = [
    [
        "bob", "password1234"
    ],
    [
        "frank", "correctpass"
    ]
]

username = input("Enter username: ")
password = input("Enter password: ")

isValidUser = False
for user in users:
    if username == user[0] and password == user[1]:
        isValidUser = True
        break

if isValidUser:
    print("Access Granted!")
else:
    print("Access Denied!")


