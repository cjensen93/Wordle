import random
import board


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
        if __checkWin(word, list(guess), i):
            break


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