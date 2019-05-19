from box import Box

class Board(object):
    def __init__(self, board_size):
        self.board = []
        for row in range(board_size):
            row = []
            for column in range(board_size):
                box = Box()
                row.append(box)
            self.board.append(row)


    def print_board(self):
        for row in self.board:
            for box in row:
                print(box.value, " ", end="")
            print("")

board = Board(2)

board.print_board()
