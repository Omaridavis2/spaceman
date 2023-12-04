import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') # comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # Loop through the letters in the secret_word and check if a letter is not in letters_guessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    return guess in secret_word

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.
    '''
    print("Welcome to Spaceman!")
    letters_guessed = []
    attempts_left = 7

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        # Check if the input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the guessed letter is in the secret word
        if is_guess_in_word(guess, secret_word):
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts_left -= 1

        letters_guessed.append(guess)

        # Show the guessed word so far
        current_guess = get_guessed_word(secret_word, letters_guessed)
        print(f"Current word: {current_guess}")

        # Check if the game has been won
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You've guessed the word.")
            break

        print(f"Attempts left: {attempts_left}")

    # Check if the player has run out of attempts
    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word}")

# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
