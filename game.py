import random
import board
import time
import sys


class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Put after every color change to revert back to normal text
    END = '\033[0m'


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


def __randomLine(textFile):
    lines = open(textFile).read().splitlines()
    myWord = random.choice(lines)
    return myWord


def __getGuess(word, index, dictionary):
    guess = True
    while guess:
        print()
        answer = str(input("Guess number " + str(index + 1) + ":  "))
        if len(answer) == word.getLength():
            lines = open(dictionary).read().splitlines()
            if answer in lines:
                return answer
            else:
                print(Colors.RED + Colors.UNDERLINE + "That word is not in our dictionary" + Colors.END)
        else:
            print(Colors.RED + Colors.UNDERLINE + "Guess must be " + str(word.getLength()) + " letters long." + Colors.END)


def __evalGuess(word, guess, index):
    for i in range(word.getLength()):
        word.guessBoard[index][i] = "[" + guess[i] + "]"
        if guess[i] == word.getWord()[i]:
            word.colorBoard[index][i] = "GREEN"
        elif guess[i] in word.getWord():
            word.colorBoard[index][i] = "YELLOW"


def __checkWin(word, guess, index):
    if word.word == guess:
        print(f"You won in {index + 1} guesses!")
        print()
        return True
    else:
        if index == word.getLength():
            print("You didn't get it. Nice try!")
            print()
        return False


def __alphaColor(word, guess):
    for i in range(word.getLength()):
        index = __getAlphaIndex(guess[i])
        if guess[i] in word.getWord():
            word.alphaColor[index] = "YELLOW"
        elif word.getWordIndex(i) == guess[i]:
            word.alphaColor[index] = "GREEN"
        else:
            word.alphaColor[index] = "NOT"

    word.printAlpha()


def __getAlphaIndex(guess):
    if guess == "a":
        return 0
    elif guess == "b":
        return 1
    elif guess == "c":
        return 2
    elif guess == "d":
        return 3
    elif guess == "e":
        return 4
    elif guess == "f":
        return 5
    elif guess == "g":
        return 6
    elif guess == "h":
        return 7
    elif guess == "i":
        return 8
    elif guess == "j":
        return 9
    elif guess == "k":
        return 10
    elif guess == "l":
        return 11
    elif guess == "m":
        return 12
    elif guess == "n":
        return 13
    elif guess == "o":
        return 14
    elif guess == "p":
        return 15
    elif guess == "q":
        return 16
    elif guess == "r":
        return 17
    elif guess == "s":
        return 18
    elif guess == "t":
        return 19
    elif guess == "u":
        return 20
    elif guess == "v":
        return 21
    elif guess == "w":
        return 22
    elif guess == "x":
        return 23
    elif guess == "y":
        return 24
    elif guess == "z":
        return 25


def __giveTime(time):
    if time <= 1:
        print(f"Game was completed in {time} second")
    elif time <= 59:
        print(f"Game was completed in {time} seconds")
    elif time > 60:
        minutes = time / 60
        seconds = time % 60
        if minutes <= 1:
            print(f"Game was completed in {minutes} minute and {seconds} seconds")
        else:
            print(f"Game was completed in {minutes} minutes and {seconds} seconds")