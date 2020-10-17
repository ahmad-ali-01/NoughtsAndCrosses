class Board:

    def __init__(self):
        self.board = [[" " for i in range(3)] for i in range(3)]

    def nought(self, x:int, y:int):
        self.board[3-y][x-1] = "O"

    def cross(self, x:int, y:int):
        self.board[3-y][x-1] = "X"

    def display(self):
        print("\n")
        for i in range(3):
            if i < 2:
                print("  " + " | ".join(self.board[i]))
                print("  " + "---------")
            else:
                print("  "+" | ".join(self.board[i]))
        print("\n")
board = Board()
board.nought(1,1)
board.cross(2,2)
board.display()
