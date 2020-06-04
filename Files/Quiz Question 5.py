
def validate_user(username, password):
    user_file = open('logins.txt', 'r')
    line = user_file.readline()
    while len(line) > 0:
        user = line.replace("\n", "").split(':')
        if user[0] == username and user[1] == password:
            user_file.close()
            return True
        line = user_file.readline()
    user_file.close()
    return False

username = input("username? ")
password = input("password? ")
if validate_user(username, password):
    print("Access Granted!")
else:
    print("Invalid username/password!")
