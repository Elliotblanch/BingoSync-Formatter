import json
import random

# Reads random line of text file
def random_line(filename):
    lines = open(filename).read().splitlines()
    return random.choice(lines)


def new_bingo(source_file):

    # Dictionary to store output
    output = []

    # Setting max length to 25
    while len(output) < 25:
        new_entry = random_line(source_file)
        # Checking for repeat entries
        if not new_entry in str(output):
            output.append({"name": new_entry})


    # Sending output to Json File
    with open('output.json', 'w') as bingo_card:
        json.dump(output, bingo_card)
    
    # Prints output in console
    print("Bingo board generated:")
    print(output)

# If using a different text file, replace 'EldenRingo.txt' with the name of your file
new_bingo('EldenRingo.txt')