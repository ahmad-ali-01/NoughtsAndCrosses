from time import sleep

class Board:

    def __init__(self):
        self.board = [[" " for i in range(3)] for i in range(3)]

    def nought(self, pos:list):
        # Places a nought on the board.
        self.board[3-pos[1]][pos[0]-1] = "O"

    def cross(self, pos:list):
        # Places a cross on the board.
        self.board[3-pos[1]][pos[0]-1] = "X"

    def get(self, pos:list):
        # Gets position from board
        return self.board[3-pos[1]][pos[0]-1]

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

def play():

  # Introduction .
  print("\nWelcome to noughts and crosses in the command line.\n")
  print("XO" * 45 + "X\n")

  # How to play.
  print("""
  Each player will see the prompt "--> " and will use a code to represent the position.
  The code is as follows:
  b = bottom, m = middle, t = top, l = left, r = right
  To reference the bottom left, the code bl would be used.  
  """)
  # Create a board.
  positions = {
  "bl":[1,1], "bm":[2,1], "br":[3,1], 
  "ml":[1,2], "mm":[2,2], "mr":[3,2],
  "tl":[1,3], "tm":[2,3], "tr":[3,3],
  "lb":[1,1], "mb":[2,1], "rb":[3,1],
  "lm":[1,2], "mm":[2,2], "rm":[3,2],
  "lt":[1,3], "mt":[2,3], "rt":[3,3]
  }
  board = Board()
  sleep(5)

  print("\nBegin!\n")

  while not board.decided():
    p1 = input("Player 1 --> ")
    while not board.get(positions[p1]) == " ":
      print("Position already filled...")
      p1 = input("Player 1 --> ")
    print("\n")
    board.nought(positions[p1])
    board.display()
    print("\n")
    if not board.decided():
      p2 = input("Player 2 --> ")
      while not board.get(positions[p2]) == " ":
        print("Position already filled...")
        p2 = input("Player 2 --> ")
      print("\n")
      board.cross(positions[p2])
      board.display()
      print("\n")
  if board.decided()[1] == "O":
    print("\nPlayer 1 wins.\n")
  else:
    print("\nPlayer 2 wins.\n")

if __name__ == "__main__":
  play()