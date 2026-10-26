import random
from idlelib.search import find_again


def generate_random_words():
    """
    Method reads 'words_alpha.txt' which contains almost all english words in existence,
    Goal is to write 3 random words to a list and print.
    """

    # making a list to store possible words
    possible_words = []
    # words_per_line defines how many words should be in a single password
    words_per_line = 3

    # read the file and store words in the list
    while True:
        # define input file and store in a variable
        input_file = "words_alpha.txt"

        # try to open the input file
        try:
            with open(input_file, 'r') as word_stream:
                # loop through the lines and strip ansi codes
                for line in word_stream:
                    cleaned_word = line.rstrip('\r\n')
                    # append cleaned lines to the list
                    possible_words.append(cleaned_word)

            break  # Exit the loop once the file is successfully read
        # print error for invalid input
        except OSError:
            print(f"\nFile '{input_file}' not found. Please try again.\n")

    word_quant = 3
    three_random_words = []

    for i in range (word_quant):
        random_index = random.randrange(len(possible_words))
        random_word = possible_words[random_index]

        three_random_words.append(random_word)

    return three_random_words


def generate_random_numbers():
    """
    Generates 3 random numbers
    """
    # Create empty numbers list
    random_numbers = []

    # defines how many numbers to generate
    num_quant = 3

    # write 3 random words to the list
    for i in range(num_quant):

        rand_num = random.randint(1,9)

        if rand_num in random_numbers:
            rand_num += 1

        random_numbers.append(str(rand_num))

    return random_numbers

def generate_random_symbols():
    """
    Generates 3 random symbols
    """
    # pool of symbols
    symbols = ["!","@","#","$","%","^","&","*",">","<",".","-","_","=","+","~","`"]
    three_random_symbols = []

    symbol_quant = 3

    for i in range(symbol_quant):
        random_index = random.randrange(len(symbols))
        random_symbol = symbols[random_index]

        three_random_symbols.append(random_symbol)

    return three_random_symbols

def create_password():
    """
    Combines 3 of each:
        Random Words
        Random Numbers
        Random Symbols

    To create a password
    """
    # call all 3 generation methods
    words = generate_random_words()
    numbers = generate_random_numbers()
    symbols = generate_random_symbols()

    # concatenate into a single list
    concatenated_password = words + numbers + symbols

    # shuffle the concatenated list
    random.shuffle(concatenated_password)

    # join concatenated list into a single string
    final_password = "".join(concatenated_password)

    print(final_password)

create_password()

