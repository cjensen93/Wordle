class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Put after every color change to revert back to normal text
    END = '\033[0m'


class Board:
    def __init__(self, wordLength, word):
        self.word = word
        self.length = wordLength
        self.guessBoard = []
        self.colorBoard = []
        self.alphaBoard = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.alphaColor = []

        self.makeBoard(self.guessBoard, ".")
        self.makeBoard(self.colorBoard, "BLANK")
        self.makeAlphaColor()

    # --------------
    # Setter Methods
    # --------------

    def setWord(self, new):
        self.word = new

    def setLength(self, new):
        self.length = new

    def setGuessBoard(self, a, b, new):
        self.guessBoard[a][b] += new

    def setColorBoard(self, a, b, new):
        self.colorBoard[a][b] += new

    # --------------
    # Getter Methods
    # --------------

    def getWord(self):
        return self.word

    def getLength(self):
        return self.length

    def getGuessBoard(self):
        return self.guessBoard

    def getColorBoard(self):
        return self.colorBoard

    def getWordIndex(self, index):
        return self.word[index]

    # --------------
    # Other Methods
    # --------------

    def makeBoard(self, board, string):
        for i in range(self.length + 1):
            board.append([])
            for j in range(self.length):
                board[i].append([string])

    def printBoard(self):
        for i in range(self.length + 1):
            printList = ""
            for j in range(self.length):
                letter = str(self.guessBoard[i][j])
                letter = letter.replace("'", "")
                if self.colorBoard[i][j] == "GREEN":
                    printList += Colors.GREEN + letter + Colors.END
                elif self.colorBoard[i][j] == "YELLOW":
                    printList += Colors.YELLOW + letter + Colors.END
                else:
                    printList += letter
            print(printList)
        print()

    def makeAlphaColor(self):
        for i in range(26):
            self.alphaColor.append("BLANK")

    def printAlpha(self):
        printList = ""
        for i in range(26):
            letter = str(self.alphaBoard[i])
            letter = letter.replace("'", "")
            if self.alphaColor[i] == "GREEN":
                printList += Colors.GREEN + "[" + letter + "]" + Colors.END
            elif self.alphaColor[i] == "YELLOW":
                printList += Colors.YELLOW + "[" + letter + "]" + Colors.END
            elif self.alphaColor[i] == "NOT":
                printList += Colors.FAIL + "[" + letter + "]" + Colors.END
            else:
                printList += "[" + letter + "]"
        print(printList)
        print()