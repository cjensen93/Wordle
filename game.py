import random
import board
import time
import sys

# List of colors for the terminal to print in
class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Put after every color change to revert to normal text
    END = '\033[0m'


# Main method that gets called to run each game iteration
def __playGame(wordLength):

    # Start a timer
    startTime = time.time()

    # Obtain a random word from the dictionary
    gameDict = "Dictionaries/" + str(wordLength) + ".txt"
    randomWord = __randomLine(gameDict).lower()
    randomWord = list(randomWord)

    # Create the word object
    word = board.Board(wordLength, randomWord)

    # Give the user (1 + the word length) guesses
    for i in range(word.getLength() + 1):

        guess = __getGuess(word, i, gameDict)
        __evalGuess(word, list(guess), i)
        word.printBoard()
        __alphaColor(word, guess)
        if __checkWin(word, list(guess), i):
            break

    # End timer, give report
    endTime = time.time()
    __giveTime(round(endTime - startTime))


# Method to choose a random word from the dictionary
def __randomLine(textFile):
    lines = open(textFile).read().splitlines()
    myWord = random.choice(lines)
    return myWord


# Method to determine what to do with the users guess
def __getGuess(word, index, dictionary):
    guess = True
    while guess:
        print()

        # Obtain the guess from the user
        answer = str(input("Guess number " + str(index + 1) + ":  "))

        # A way, as described in the README, to let the user leave the game
        if answer == "!!!":
            print("Thanks for playing!")
            sys.exit(0)

        # Checks to see if the user has already guessed that word
        elif answer in word.guessesList:
            print(Colors.RED + Colors.UNDERLINE + "Cannot guess a word that has already been used" + Colors.END)

        # Checks to make sure the word is the correct length
        elif len(answer) == word.getLength():

            # Checks the dictionary to see if the guess was a valid word
            lines = open(dictionary).read().splitlines()
            if answer in lines:
                word.guessesList.append(answer)
                return answer

            # If it's not in the dictionary, inform the user
            else:
                print(Colors.RED + Colors.UNDERLINE + "That word is not in our dictionary" + Colors.END)

        # If the guess isn't the right length of letters, inform the user
        else:
            print(Colors.RED + Colors.UNDERLINE + "Guess must be " + str(word.getLength()) + " letters long." + Colors.END)


# Sets the color of each letter of the guess, based on its correctness
def __evalGuess(word, guess, index):
    for i in range(word.getLength()):
        word.guessBoard[index][i] = "[" + guess[i] + "]"

        # If the letter is in the word and in the correct spot, turn it green
        if guess[i] == word.getWord()[i]:
            word.colorBoard[index][i] = "GREEN"

        # If the letter is in the word but not in the correct spot, turn it yellow
        elif guess[i] in word.getWord():
            word.colorBoard[index][i] = "YELLOW"


# Method to see if the user won the game. Is called after every valid guess
def __checkWin(word, guess, index):

    # Checks if the guess is the correct word
    if word.word == guess:
        print(f"You won in {index + 1} guesses!")
        print()
        return True

    # Checks if the user has used all of their guesses
    else:
        if index == word.getLength():
            correctWord = ''
            for x in word.word:
                correctWord += str(x)

            print("You didn't get it. Nice try!")
            print(f"The word was '{correctWord}'")
            print()
        return False


# Sets the color of the alphabet list, based on if its correctness
def __alphaColor(word, guess):
    for i in range(word.getLength()):
        index = __getAlphaIndex(guess[i])
        if word.getWordIndex(i) == guess[i]:
            word.alphaColor[index] = "GREEN"
        elif guess[i] in word.getWord():
            word.alphaColor[index] = "YELLOW"
        else:
            word.alphaColor[index] = "NOT"

    word.printAlpha()


# Converts the alphabet into a much easier to use number
def __getAlphaIndex(guess):
    match guess:
        case "a":
            return 0
        case "b":
            return 1
        case "c":
            return 2
        case "d":
            return 3
        case "e":
            return 4
        case "f":
            return 5
        case "g":
            return 6
        case "h":
            return 7
        case "i":
            return 8
        case "j":
            return 9
        case "k":
            return 10
        case "l":
            return 11
        case "m":
            return 12
        case "n":
            return 13
        case "o":
            return 14
        case "p":
            return 15
        case "q":
            return 16
        case "r":
            return 17
        case "s":
            return 18
        case "t":
            return 19
        case "u":
            return 20
        case "v":
            return 21
        case "w":
            return 22
        case "x":
            return 23
        case "y":
            return 24
        case "z":
            return 25


# Function for reporting the game's time in the correct units
def __giveTime(timer):

    # Method incase the user somehow finishes in less than one second
    if timer <= 59:
        secondWord = "second" if timer < 2 else "seconds"
        print(f"Game was completed in {timer} {secondWord}")

    # Method for if the game was over one minute
    else:
        minutes = timer // 60
        seconds = timer % 60
        minuteWord = "minute" if minutes < 2 else "minutes"
        secondWord = "second" if seconds < 2 else "seconds"
        print(f"Game was completed in {minutes} {minuteWord} and {seconds} {secondWord}")
