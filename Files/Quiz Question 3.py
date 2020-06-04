name_file = open('names.txt', 'r')
out_file = open('names-formatted.txt', 'w')
line = name_file.readline()
while len(line) > 0:
    name = line.lower().split(' ')
    newName = []
    for word in name:
        word = word[0].upper() + word[1:len(word)]
        newName.append(word)
    newName = ' '.join(newName)
    out_file.write(newName)
    line = name_file.readline()
name_file.close()
out_file.close()
