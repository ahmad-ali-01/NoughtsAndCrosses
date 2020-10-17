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

    def solved(self):
        # Returns true if the game has been decided otherwise false.
        self.boolboard = [[True if self.board[j][i] == "O" else False if self.board[j][i] == "X" else None for i in range(3)] for j in range(3)]
        return self.boolboard

board = Board()
board.nought(1,1)
board.cross(2,2)
board.display()
print(board.solved())
