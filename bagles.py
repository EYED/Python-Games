# -*- coding: utf-8 -*-
"""
this is the game bagels.
you get ten guesses to guess a non repeating 3 digit number.
Written with Python 2.6.5

"""
#------------------------------------------------------------------------------|
#                                                                              |
# Imports                                                                      |
#                                                                              |
#------------------------------------------------------------------------------|

import random

#------------------------------------------------------------------------------|
#                                                                              |
#   function getSecretNumber ( maxNumber )                                     |
#   this function is to get the number that the player has to guess            |
#   arguments:                                                                 |
#       - maxNumber this argument is used to prevent the computer from making a|
#           number with more than three digits                                 |
#   returns:                                                                   |
#       - this function returns the secret number to the playersGuess function |
#                                                                              |
#------------------------------------------------------------------------------|

def getSecretNumber ( maxNumber ):
    digits = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle( digits )
    secretNumber = []
    for numbers in range(maxNumber):
        secretNumber.append(digits[numbers])
    return secretNumber

#------------------------------------------------------------------------------|
#                                                                              |
#   function playersGuess (maxGuesses , maxNumber )                            |
#   this function is to get the players guess and send it to the checking      |
#       function guessChecker                                                  |
#   arguments:                                                                 |
#       - maxGuesses this is a variable that holds the most amount of guesses  |
#           that a player can guess before they fail                           |
#       - maxNumber this is the variable that holds the info on the most amount|
#           of digits the secret number can be (which is three)                |
#   returns:                                                                   |
#       - win which is set to 1 if the player guesses right                    |
#       - fail which is set to 2 and only return in the event that the player  |
#           does not correctly guess the number before guesses becomes equal to|
#           maxGuesses                                                         |
#       - secNum is the secret number your trying to guess and is sent so that |
#           the computer will tell you what the number you were trying to guess|
#           is.                                                                |
#                                                                              |
#------------------------------------------------------------------------------|

def playersGuess ( maxGuesses , maxNumber ):
    secNum = getSecretNumber(maxNumber) #secNum is short for secretNumber
    guesses = 1
    win = None
    while guesses <= maxGuesses and (win is None):
        playersGuess = []
        while len(playersGuess) < 3:
            guessType = ["first","second","third"]
            print "You have guessed %s time(s)." %(guesses)
            playersGuess.append(int(input("What is your %s number?>" %(guessType[len(playersGuess)]) ) ) )
        win = guessChecker( secNum , playersGuess , maxNumber )
        guesses += 1
    if guesses == maxGuesses and (win is None):
        return False , secNum
    else:
        return win , secNum

#------------------------------------------------------------------------------|
#                                                                              |
#   function guessChecker ( secNum , plaGuess , maxNumber )                    |
#   this function is designed to check for the guess being right. if its not   |
#   right then it checks to see if you had some right numbers and sets the clues
#   you get then prints those clues.                                           |
#   arguments:                                                                 |
#       - secNum is short for secretNumber and is the number that you checking |
#           against.                                                           |
#       - plaGuess is short for playersGuess and is the number that is being   |
#           checked.                                                           |
#       - maxNumber is the variable that holds the most amount of digits that  |
#           secretNumber can hold. is used here to indicate the range that the |
#           for loop for giving clues is used                                  |
#   returns:                                                                   |
#       - returns True if the guess was correct                                |
#       - else returns None                                                    |
#                                                                              |
#------------------------------------------------------------------------------|

def guessChecker ( secNum , plaGuess , maxNumber):
    if plaGuess == secNum:
        return True
    clue = []
    for numeral in range( maxNumber ):
        if plaGuess[numeral] == secNum[numeral]:
            clue.append("Pico")
        elif plaGuess[numeral] in secNum:
            clue.append("Fermi")
    if len(clue) == 0:
        clue.append("Bagels")
    print " ".join(clue)
    return None

#------------------------------------------------------------------------------|
#                                                                              |
#   function again()                                                           |
#   this is a simple function used to check if the player wants to play again. |
#   there are no arguments as its a simple check.                              |
#   returns:                                                                   |
#       - returns True if the player says yes                                  |
#       - otherwise returns False                                              |
#                                                                              |
#------------------------------------------------------------------------------|

def again():
    return raw_input("Play again? (yes or no)>").lower().startswith("y")

#------------------------------------------------------------------------------|
#                                                                              |
#   this area is where the conrol loop for the game will start. it also defines|
#   the constant variables to be used.                                         |
#   constant variables:                                                        |
#       - MAXGUESSES is the variable that holds the most guess a player can do |
#           before he/she fails.                                               |
#       - MAXNUMBER is the variable that holds the most digits the secret number
#           can be.                                                            |
#                                                                              |
#------------------------------------------------------------------------------|

MAXGUESSES = 10
MAXNUMBER = 3
againCheck = True
while againCheck is True:
    print """
Let's play Bagels. I'll think of a three digit number. It will use the numerals
0 to 9 and will not repeat. You have %s guesses to get it right. Don't dispair
though! I'll give you clues to help you out.
If I say:           That means:
Pico                A number is right and in the right location, but I won't say which.
Fermi               A number is right but in the wrong location.
Bagles              None of the numbers is right.
Let's get started.""" %(MAXGUESSES)
    won , secNum = playersGuess ( MAXGUESSES , MAXNUMBER ) #secNum is short for secretNumber
    if won is False:
        print "I'm sorry. My number was %s. Try again." %(secNum)
    elif won is True:
        print "Yes! that was my number!"
    againCheck = again()
quit()
