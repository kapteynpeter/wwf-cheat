from .. import game_info as info

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
                self.addLetter(x, y+i, letter)
    
    ''' finish this function '''
    def evaluateWord(self, x, y, ori, word):
        wordval = 0
        if ori == info.UP:
            for i, letter in enumerate(word):
                wordval = wordval + info.letter_values[letter] * info.char_map[x-i][y]
        if ori == info.DOWN:
            for i, letter in enumerate(word):
                wordval = wordval + info.letter_values[letter] * info.char_map[x+i][y]
        if ori == info.LEFT:
            for i, letter in enumerate(word):
                wordval = wordval + info.letter_values[letter] * info.char_map[x][y-i]
        if ori == info.RIGHT:
            for i, letter in enumerate(word):
                wordval = wordval + info.letter_values[letter] * info.char_map[x][y+i]
        return wordval        

    def getAvailableLetters(self):
        pass

    

    def out(self):
        for row in self.board:
            print(row)

board = Board()