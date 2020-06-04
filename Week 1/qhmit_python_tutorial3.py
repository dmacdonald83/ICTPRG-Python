def get_three_inputs():
    result = []
    result.append(input("Input 1 (Name): "))
    result.append(input("Input 2 (Verb): "))
    result.append(input("Input 3 (Noun): "))
    return result


def print_first(inputs):
    print("Hey '" + inputs[0] + "'! Stop '" + inputs[1] + "' my '" + inputs[2] + "'.")

def print_second(inputs):
    print("'" + inputs[0] + "' once '" + inputs[1] + "' and walked out with '" + inputs[2] + "'.")



inputs = get_three_inputs()
print_first(inputs)
inputs = get_three_inputs()
print_second(inputs)
