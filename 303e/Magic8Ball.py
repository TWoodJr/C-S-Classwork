#-------------------------------------------------------------------------------
# Name:        Assignment 2
# Purpose:     Magic 8 ball Q/A
#
# Author:      Terry Woodard
#
# Created:     05/02/2018
# Copyright:   (c) terry_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

answerList = ['Yes', 'No', 'Yes, but not now', 'Um, definiely no', 'That is a terrible idea',
              'Why would you even ask that', 'Only on Sundays', "Only if you don't want lunch",
              "You really wasted a question on that but sure", "Not likely", "Ask me again",
              "Probably", "It's gonna be a no from me", "Enthusiastic Yes", "Only if YOU believe"]

name = input("What is your name?")
q = input("What is your question?")
ans = random.randint(0, 14)
print ("Welcome to the Virtual Magic 15 Ball Program")
print ("Hello " + name)
print ("What is your question? " + q)
print (name + ", your answer is: " + answerList[ans])
