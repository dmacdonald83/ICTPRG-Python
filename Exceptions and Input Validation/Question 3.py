def GetWordsFromUser(min, max):
    words = input("Enter words: ")
    count = len(words.split(' '))
    while count < min or count > max:
        words = input("Enter words: ")
        count = len(words.split(' '))
    return words.lower().split(' ')

