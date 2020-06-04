def char_to_morse(ch):
    morse = [
        #A to Z
        '.-', '-...', '-.-.', '-..', '.', '..-.', 
        '--.', '....', '..', '.---', '-.-', '.-..', 
        '--', '-.', '---', '.--.', '--.-', '.-.', 
        '...', '-', '..-', '...-', '.--', '-..-', 
        '-.--', '--..',
        #1,2,3,4,5,6,7,8,9,0
        '.----', '..---', '...--', '....-', '.....',
        '-....', '--...', '---..', '----.', '-----'
    ]
    return morse[ord(ch.lower()[0]) - 97]

def string_to_morse(string):
    output = ''
    for x in string:
        if x == ' ':
            output += '\n'
        else:
            output += char_to_morse(x) + ' '
    return output

print(string_to_morse('this is a test'))

