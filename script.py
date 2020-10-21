class Board:

    def __init__(self):
        self.board = [[" " for i in range(3)] for i in range(3)]

    def nought(self, x:int, y:int):
        # Places a nought on the board.
        self.board[3-y][x-1] = "O"

    def cross(self, x:int, y:int):
        # Places a cross on the board.
        self.board[3-y][x-1] = "X"

    def display(self):
        # Displays the board.
        print("\n")
        for i in range(3):
            if i < 2:
                print("  " + " | ".join(self.board[i]))
                print("  " + "---------")
            else:
                print("  "+" | ".join(self.board[i]))
        print("\n")

    def streams(self):
        # Returns a list with each element being a list containing a possible winning position.
        positions = [i for i in self.board] + \
        [[self.board[i][j] for i in range(3)] for j in range(3)] + \
        [[self.board[i][i] for i in range(3)]] +\
        [[self.board[2-i][i] for i in range(3)]]
        return positions

    @staticmethod
    def possible():
        return [["O" for i in range(3)], ["X" for i in range(3)]]

    def decided(self):
        for i in  self.streams():
            if i in Board.possible():
                return [True, i[0]]
        return False
