import secrets

def apply_capitalization(word_list):
    """
    Internal helper to randomly capitalize letters
    """
    capitalized_words = []

    for word in word_list:
        cap_word = ""

        for char in word:
            if secrets.randbelow(2) == 0:
                cap_word += char.upper()
            else:
                cap_word += char

        capitalized_words.append(cap_word)

    return capitalized_words

def generate_random_words():
    """
    Method reads 'words_alpha.txt' which contains almost all english words in existence,
    Writes 4 random words to a list.
    """

    # making a list to store possible words
    possible_words = []
    # word_quant defines how many words should be in a single password
    word_quant = 4
    # list to store randomly generated words
    random_words = []

    # read the file first and store all possible words in a list
    while True:
        # define input file and store in a variable
        input_file = "words_alpha.txt"

        # try to open the input file
        try:
            with open(input_file, 'r') as word_stream:
                # loop through the lines and strip ansi codes
                for line in word_stream:
                    cleaned_word = line.rstrip('\r\n')
                    # append cleaned lines to the list only if the word has 5 characters or more
                    if len(cleaned_word) >= 5:
                        possible_words.append(cleaned_word)

            break  # Exit the loop once the file is successfully read
        # print error for invalid input
        except OSError:
            print(f"\nFile '{input_file}' not found. Please try again.\n")

    # Loop fills the random_word list with amount of random words defined by word_quant
    for i in range (word_quant):
        # Using secrets for cryptographic randomness
        # Select a random index in the list of possible words
        random_index = secrets.randbelow(len(possible_words))
        # Get the word stored in that index
        random_word = possible_words[random_index]
        # Append the random word to the list
        random_words.append(random_word)

    return random_words

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

        # Using secrets.randbelow instead of random.randint for cryptographic randomness.
        rand_num = secrets.randbelow(9)+1

        # preventing duplicate numbers (may be less secure, I'm not sure)
        if rand_num in random_numbers:
            rand_num += 1

        # append the random number to the list as a string
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

    # Loop generates 3 random symbols
    for i in range(symbol_quant):
        # Using secrets.randbelow instead of random.randint for cryptographic randomness.
        random_index = secrets.randbelow(len(symbols))
        # get the random symbol using the random index
        random_symbol = symbols[random_index]
        # append to the random symbol list
        three_random_symbols.append(random_symbol)

    return three_random_symbols

def apply_character_swap(word_list):
    # a dictionary to store common leetspeak letter swaps
    swaps = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }

    # list to store modified words
    swapped_word_list = []

    # a loop to iterate through each word and apply character swap
    for word in word_list:
        swapped_word = ""
        # iterate through each character in each word
        for char in word:
            # use a 50/50 chance to apply character swap (not sure if this adds entropy
            fifty_fifty_chance = secrets.randbelow(2)

            # if the character exits in the swaps dict, and 50/50 chance
            if char in swaps and fifty_fifty_chance == 0:
                # apply character swap
                swapped_word += swaps[char]
            else:
                # else apply regular character
                swapped_word += char
        # append swapped words to the list
        swapped_word_list.append(swapped_word)

    return swapped_word_list


def create_password():
    """
    RUN THIS! - Uses internal methods to generate a random password
    """


    # call the generate words method
    words = generate_random_words()
    print(f"\nGenerating 4 random Words: \n{words}")
    # apply character swaps on the words list
    swapped_words = apply_character_swap(words)
    print(f"\nApplying character swaps on the words: \n{swapped_words}")
    # apply capitalization on the words list
    final_words = apply_capitalization(swapped_words)
    print(f"\nApply capitalization on the words: \n{final_words}")

    # generate random numbers and symbols
    numbers = generate_random_numbers()
    symbols = generate_random_symbols()

    # concatenate into a single list
    concatenated_password = final_words + numbers + symbols
    print(f"\nConcatenating list with random numbers and symbols: \n{concatenated_password}")

    # shuffle the concatenated list
    for i in range(5):
        secrets.SystemRandom().shuffle(concatenated_password)
    print(f"\nShuffling the concatenated list: \n{concatenated_password}")

    # join concatenated list into a single string
    final_password = "".join(concatenated_password)
    print(f"\nJoin the list into a single string: \n{final_password}")

    return final_password