
from .board import Board
from . import game_info as info

class WwfApp():
   
    def __init__(self):
        self.board = Board()
    
    def run(self):
        print(self.board.addWord)
