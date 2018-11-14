#-------------------------------------------------------------------------------
'''
 File:          MagicSquare.py
 Description:   Create magic square matrices
 Student Name:  Terry Woodard
 EID:           tgw466
 Partner:       Jerry Che
 Partner EID:   jc78222
 Course:        CS 313E
 Unique Number: 86325
 Created:       16/06/2018
 Date Last Modified: 17/06/2018
'''
#-------------------------------------------------------------------------------

#Populate a 2-D list with numbers from 1 to n**2
#This function must take as input an integer. You may assume that
#n >= 1 and n is odd. This function must return a 2-D list (a list of
#lists of integers) representing the square.
#Example 1: make_square(1) should return [[1]]
#Example 2: make_square(3) should return [[4,9,2],[3,5,7],[8,1,6]]
def make_square(n):
    square = [[None for x in range(n)] for y in range(n)]
    #sets position of 1 and the number
    num = 1
    i = n-1
    j = n//2
    while num <= n**2:
        #check if it falls out of bottom bound
        if i == n:
            i = 0
        #check if it falls out of right bound
        if j == n:
            j = 0
        #check if it is in right corner
        if (i == n) and (j == n):
            i = i-2
            j = j-1

        #check if square is filled
        if square[i][j] != None:
            i = i-2
            j = j-1
            continue
        #fill square
        else:
            square[i][j] = num
            num += 1
        #change position right and down
        i += 1
        j += 1

    return square
    print square
#Print the magic square in a neat format where the numbers
#are right justified
#This function must take as input a 2-D list of integers
#This function does not return any value
#Example: Calling print_square(make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square(magic_square):
    for i in range(len(magic_square)):
        row = str(magic_square[i]).strip('[]')
        print row.replace(',', '')

#Check that the 2-D list generated is indeed a magic square
#This function must take as input a 2-D list, and return a boolean
#Example 1: check_square([[1,2],[3,4]]) should return False
#Example 2: check_square([[4,9,2],[3,5,7],[8,1,6]]) should return True
def check_square(magic_square):
    n = len(magic_square)
    cannonicalSum = int((n *((n**2)+1)) / 2)
    vertSum = 0
    diagSum = 0
    for i in range(len(magic_square)):
        rowSum = sum(magic_square[i])
        vert = magic_square[i][0]
        diag = magic_square[i][i]
        vertSum += vert
        diagSum += diag

    if (cannonicalSum == rowSum) and (cannonicalSum == vertSum) and (cannonicalSum == diagSum):
        print "This is a magic square and the cannonical sum is", cannonicalSum
        return True
    else:
        print "This is not a magic square"
        return False


def main():
    #Prompt the user to enter an odd number 1 or greater
    magic_square = int(raw_input("Please enter an odd number: "))
    #Check the user input
    while (magic_square <= 0) or (magic_square % 2 == 0):
        magic_square = int(raw_input("Please enter an odd number: "))
    #Create the magic square
    print "Here is a", magic_square, "x", magic_square, "magic square:"
    newSquare = make_square(magic_square)
    #Print the magic square
    print_square(newSquare)
    #Verify that it is a magic square
    check_square(newSquare)

#This line above main is for grading purposes. It will not affect how
#your code will run while you develop and test it.
#DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == '__main__':
    main()
