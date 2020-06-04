

names = []

name = input("Enter name: ")
while len(name) > 0:
    names.append(name)
    name = input("Enter name: ")

out_file = open('people.txt', 'w')
for n in names:
    out_file.write(n + "\n")
out_file.close()
