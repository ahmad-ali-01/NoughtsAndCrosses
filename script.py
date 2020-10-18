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

    def decided(self):
        # Returns [true, board value] if the game has been decided otherwise false.
        self.boolboard = self.board
        if (self.boolboard[0][0] == self.boolboard[0][1]) and (self.boolboard[0][1] == self.boolboard[0][2]):
            return [True, self.boolboard[0][0]]
        elif (self.boolboard[1][0] == self.boolboard[1][1]) and (self.boolboard[1][1] == self.boolboard[1][2]):
            return [True, self.boolboard[1][0]]
        elif (self.boolboard[2][0] == self.boolboard[2][1]) and (self.boolboard[2][1] == self.boolboard[2][2]):
            return [True, self.boolboard[2][0]]
        elif (self.boolboard[0][0] == self.boolboard[1][0]) and (self.boolboard[1][0] == self.boolboard[2][0]):
            return [True, self.boolboard[0][0]]
        elif (self.boolboard[0][1] == self.boolboard[1][1]) and (self.boolboard[1][1] == self.boolboard[2][1]):
            return [True, self.boolboard[0][1]]
        elif (self.boolboard[0][2] == self.boolboard[1][2]) and (self.boolboard[1][2] == self.boolboard[2][2]):
            return [True, self.boolboard[0][2]]
        elif (self.boolboard[0][0] == self.boolboard[1][1]) and (self.boolboard[1][1] == self.boolboard[2][2]):
            return [True, self.boolboard[0][0]]
        elif (self.boolboard[0][2] == self.boolboard[1][1]) and (self.boolboard[1][1] == self.boolboard[2][0]):
            return [True, self.boolboard[0][2]]
        return False

board = Board()
board.nought(1,1)
board.cross(2,2)
board.display()
print(board.decided())
