#-------------------------------------------------------------------------------
# Name:        Assignment 5
# Purpose:     Mastermind Codebreaker
#
# Author:      Terry Woodard
#
# Created:     15/04/2018
# Copyright:   (c) terry_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


code = open("input.txt", "r")
code.readline()

userGuess = raw_input("Guess: ")
print userGuess

def checkGuess(userGuess):
    answers = ["R","G","Y","O","P","B"]
    for x in userGuess:
        if x not in answers:
            print "Error"

def getFeedback():
    guess = list(userGuess)
    feedback = list("----")
    for x in feedback:
        for y in guess:
            if feedback[x] == guess[y]:
                feedback[x] = guess[x]
        if feedback[x] in guess:
            feedback[x] = "W"
    print "Feedback: " + "".join(feedback)

def didYouWin(guesses = 0):
    tryAgain = userGuess
    while guesses <= 10:
        if code == userGuess or code == tryAgain:
            print "You win!"
            break
        else:
            print "Score: -{0}".format(guesses)
            guesses += 1
            tryAgain = raw_input("Guess: ")


def main():
    print "Guess: " + userGuess
    checkGuess(userGuess)
    getFeedback()
    didYouWin()

main()





