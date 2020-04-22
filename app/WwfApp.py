
from .board import Board

class WwfApp():
   
    def __init__(self):
        self.board = Board()
    
    def run(self):
        self.board.addLetter(0,0,'x')
