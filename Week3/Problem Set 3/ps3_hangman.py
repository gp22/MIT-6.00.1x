# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return_string = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return_string += '_ '
        else:
            return_string += letter
    return return_string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available_letters += letter
    
    return available_letters    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 8
    letters_guessed = []
    current_guess = ''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    # main game loop
    while not isWordGuessed(secretWord, letters_guessed):
        print('-------------')
        print('You have', num_guesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(letters_guessed))
    
        current_guess = (input('Please guess a letter: '))
        # check if they've already guessed this letter        
        if current_guess in letters_guessed:
            print("Oops! You've already guessed that letter:", \
                   getGuessedWord(secretWord, letters_guessed))
            continue
        elif current_guess in secretWord:
            letters_guessed.append(current_guess)
            print("Good guess:", getGuessedWord(secretWord, letters_guessed))
            if isWordGuessed(secretWord, letters_guessed):
                print('Congratulations, you won!')                
                return 'Congratulations, you won!'
                break
            else: continue
        else:
            letters_guessed.append(current_guess)
            print("Oops! That letter is not in my word:", \
                   getGuessedWord(secretWord, letters_guessed))
            num_guesses -= 1
            if num_guesses == 0:
                print('Sorry, you ran out of guesses. The word was:', secretWord)
                return_string = 'Sorry, you ran out of guesses. The word was:' + secretWord
                return return_string
                break
            else: continue
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'apple'
hangman(secretWord)
