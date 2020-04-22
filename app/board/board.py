from . import game_info

BOARD_WIDTH  = 15
BOARD_HEIGHT = 15



'''
Maybe add a way to store a temporary word, then call setWord() to make it permanent
Add checks for addLetter and addWord to make sure the x and y have to be within range
'''
class Board():

    def __init__(self):
        self.board = [''] * BOARD_WIDTH
        for i in range(BOARD_WIDTH):
            self.board[i] = [''] * BOARD_HEIGHT

    def addLetter(self, x, y, letter):
        self.board[x][y] = letter

    def addWord(self, x, y, ori, word):
        if ori == info.UP:
            for i, letter in enumerate(word):
                self.addLetter(x-i, y, letter)
        if ori == info.DOWN:
            for i, letter in enumerate(word):
                self.addLetter(x+i, y, letter)
        if ori == info.LEFT:
            for i, letter in enumerate(word):
                self.addLetter(x, y-i, letter)
        if ori == info.RIGHT:
            for i, letter in enumerate(word):
                self.addLetter(x-i, y+i, letter)

    def getAvailableLetters(self):
        pass

    def evaluateWord(self):
        pass

board = Board()