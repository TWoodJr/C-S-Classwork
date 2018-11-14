#-------------------------------------------------------------------------------
  # File: Queens.py

  # Description: solve the queens problem

  # Student's Name: Terry Woodard

  # Student's UT EID: tgw466

  # Partner's Name: Jerry Che

  # Partner's UT EID: jc78222

  # Course Name: CS 313E

  # Unique Number: 86325

  # Date Created: 7/18/2018

  # Date Last Modified: 7/20/2018
#-------------------------------------------------------------------------------

class Queens:
    #initialize the baord
    def __init__(self, n):
        self.n = n
        self.solutions = 0

    #check if no queen captures another
    def isValid(self, pos, row, col):
        for i in range(row):
            if pos[i] == col or \
                pos[i] - i == col - row or \
                pos[i] + i == col + row:

                return False
        return True

    #solve the problem
    def solve(self):
        positions = [-1] * self.n
        self.recursiveSolve(positions, 0)
        print "There are " + str(self.solutions) + " solutions for a " + str(self.n) + " x " + str(self.n) + " board."

    def recursiveSolve(self, pos, row):
        if row == self.n:
            self.printBoard(pos)
            self.solutions += 1
        else:
            for col in range(self.n):
                if self.isValid(pos, row, col):
                    pos[row] = col
                    self.recursiveSolve(pos,row + 1)

    #print the board
    def printBoard(self, pos):
        for row in range(self.n):
            line = ""
            for column in range(self.n):
                if pos[row] == column:
                    line += "Q "
                else:
                    line += "* "
            print(line)
        print("\n")


def main():
    #create object
    size = int(input("Enter the board size:"))
    while size < 1 or size > 8:
        size = int(input("Enter the board size:"))

    queens = Queens(size)
    queens.solve()


if __name__ == "__main__":
    main()
