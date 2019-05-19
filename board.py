import random
from box import Box

class Board(object):
    def __init__(self, size):
        self.size = size
        self.board = []
        for row in range(size):
            row = []
            for column in range(size):
                box = Box()
                row.append(box)
            self.board.append(row)

    def generate_mines(self, mines):
        while mines > 0:
            row = random.randint(0, self.size - 1)
            column = random.randint(0, self.size - 1)
            box = self.board[row][column]
            if box.has_bomb():
                continue
            box.value = -1
            mines -= 1

    def print_board(self):
        for row in self.board:
            for box in row:
                print(box.value, " ", end="")
            print("")

board = Board(4)
board.generate_mines(2)
board.print_board()
