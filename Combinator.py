import random
import secrets


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
    capitalized_words = []

    for i in range (word_quant):
        random_index = secrets.randbelow(len(possible_words))
        random_word = possible_words[random_index]

        three_random_words.append(random_word)

    for word in three_random_words:
        cap_word = ""

        for char in word:
            if secrets.randbelow(2) == 0:
                cap_word += char.upper()
            else:
                cap_word += char

        capitalized_words.append(cap_word)

    return capitalized_words


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

        rand_num = secrets.randbelow(9)+1

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
        random_index = secrets.randbelow(len(symbols))
        random_symbol = symbols[random_index]

        three_random_symbols.append(random_symbol)

    return three_random_symbols

def apply_character_swap(word_list):
    # a dictionary to store common letter swaps
    swaps = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }

    # a translation table executes multiple character swaps in a single pass
    translation_table = str.maketrans(swaps)

    # list to store modified words
    swapped_word_list = []

    # a loop to iterate through each word and apply character swap
    for word in word_list:
        swapped_word = ""
        for char in word:
            fifty_fifty_chance = secrets.randbelow(2)

            if char in swaps and fifty_fifty_chance == 0:
                swapped_word += swaps[char]
            else:
                swapped_word += char

        swapped_word_list.append(swapped_word)

    return swapped_word_list


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
    print(words)

    swapped_words = apply_character_swap(words)

    numbers = generate_random_numbers()
    symbols = generate_random_symbols()

    # concatenate into a single list
    concatenated_password = swapped_words + numbers + symbols

    # shuffle the concatenated list
    for i in range(5):
        secrets.SystemRandom().shuffle(concatenated_password)


    # join concatenated list into a single string
    final_password = "".join(concatenated_password)

    print(final_password)

create_password()

