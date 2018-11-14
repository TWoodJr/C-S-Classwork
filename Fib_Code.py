#-------------------------------------------------------------------------------
# Name:        Assignment 3
# Purpose:     Fibonacci word coder
#
# Author:      Terry Woodard Jr
#
# Created:     07/03/2018
#-------------------------------------------------------------------------------

fibNums = [0, 1]
for i in range(2,700):
    fibNums.append(fibNums[i-1]+fibNums[i-2])

userInput = input("Enter a number, a ';', then a word")
if userInput.find(";") != -1:
        fibStart, codeWord = userInput.split(";")
elif eval(userInput) < 1:
    quit()

while int(fibStart) > 0:
    newCode = ""
    for l in range(len(codeWord)):
        letter = codeWord[l:l+1]
        letNum = ord(letter.upper()) - 64
        addN = letNum + fibNums[int(fibStart)-1]
        modN = addN % 26
        if modN == 0:
            newLetter = "Z"
        else:
            newLetter = chr(modN+64)
        newCode+=newLetter
        fibStart = int(fibStart) + 1

    print (newCode)
    userInput = input("Enter a number, a ';', then a word")
    if userInput.find(";") != -1:
        fibStart, codeWord = userInput.split(";")
    elif eval(userInput) < 1:
        break

