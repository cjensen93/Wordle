import game

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


def __main():
    __introMessage()

    # Create main game loop
    continuePlaying = True
    while continuePlaying:

        # Obtain the length of word the user wants to play with
        wordLength = __numberInput()

        # Start the game
        game.__playGame(wordLength)

        # Ask to keep playing
        continuePlaying = __keepPlaying()

    # Print exit message
    print("")
    print(Colors.PURPLE + "Thank you for playing!" + Colors.END)


def __keepPlaying():
    yesList = ("YES", "Yes", "yes", "Y", "y")
    noList = ("NO", "No", "no", "N", "n")

    selection = True
    while selection:
        answer = str(input("Would you like to play again? (Y/N):  "))
        if answer in yesList:
            return True
        elif answer in noList:
            return False
        else:
            print(Colors.UNDERLINE + "Incorrect input. Type 'Y' or 'N'" + Colors.FAIL)


def __introMessage():
    print("")
    print(Colors.PURPLE + "            Welcome to")
    print(" __    __              _ _       ")
    print("/ / /\ \ \___  _ __ __| | | ___  ")
    print("\ \/  \/ / _ \| '__/ _` | |/ _ \ ")
    print(" \  /\  / (_) | | | (_| | |  __/ ")
    print("  \/  \/ \___/|_|  \__,_|_|\___| ")
    print("")
    print("       Python Edition")
    print(Colors.BOLD + "          By Caleb Jensen" + Colors.END)
    print("")


def __numberInput():
    selection = True
    while selection:

        print(Colors.GREEN + "  Easy mode: 4 letters" + Colors.END)
        print(Colors.YELLOW + "Normal mode: 5 letters" + Colors.END)
        print(Colors.RED + "  Hard mode: 6 letters" + Colors.END)
        print(Colors.BLUE + "   Insanity: 7 letters" + Colors.END)
        inputLength = input("How many letters do you want in your word? (4 - 7):  ")
        try:
            inputLength = int(inputLength)
            if inputLength >= 4:
                if inputLength <= 7:
                    return inputLength
                else:
                    print(Colors.UNDERLINE + "Number must be less than or equal to 7" + Colors.END)
            else:
                print(Colors.UNDERLINE + "Number must be greater than or equal to 4" + Colors.END)
        except ValueError:
            print(Colors.UNDERLINE + "Input MUST be integers between 4 and 7" + Colors.END)