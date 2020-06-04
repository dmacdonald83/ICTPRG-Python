words = input("Enter some words: ")
word_list = words.split()
print("You entered", len(word_list), "words.")
print("a. The first word:", word_list[0])
if len(word_list) >= 3:
    print("b. The third word:", word_list[2])
    print("c. Every word excluding the first and last:", ' '.join(word_list[1:-1]))
