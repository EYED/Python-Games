# -*- coding: utf-8 -*-
"""
This is a game where the player has to find 3 chests in an ocean. They get to
use 16 sonar devices to find the chests. each sonar device can detect a chest
up to 9 squares away from where the player places it. ie where D is the sonar:

9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9
9 8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 9
9 8 7 6 6 6 6 6 6 6 6 6 6 6 6 6 7 8 9
9 8 7 6 5 5 5 5 5 5 5 5 5 5 5 6 7 8 9
9 8 7 6 5 4 4 4 4 4 4 4 4 4 5 6 7 8 9
9 8 7 6 5 4 3 3 3 3 3 3 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 2 2 2 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 1 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 D 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 1 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 2 2 2 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 3 3 3 3 3 3 4 5 6 7 8 9
9 8 7 6 5 4 4 4 4 4 4 4 4 4 5 6 7 8 9
9 8 7 6 5 5 5 5 5 5 5 5 5 5 5 6 7 8 9
9 8 7 6 6 6 6 6 6 6 6 6 6 6 6 6 7 8 9
9 8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 9
9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9
9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9

Written with Python 2.6.5

"""

#===============================================================================|
#                                                                               |
#   Imports                                                                     |
#                                                                               |
#===============================================================================|

import sys
import random

#===============================================================================|
#                                                                               |
# function createXYBoard()                                                      |
#   this function is used to make a multidimensional list that will be used to  |
#   have x,y coordinates in the sonar game we call it xyBoard because in a later|
#   function we create a copy of the board for printing easier printing of the  |
#   board. we first use a range to append 60 lists to the list xyBoard. this    |
#   will be our x axis. then we use a range to append random charachters to the |
#   new list withing the list that we just created. this will be the y axis.    |
# arguments:                                                                    |
#   none                                                                        |
# returns:                                                                      |
#   the list of lists xyBoard which is used to do all the calculations in       |
#       game.                                                                   |
#                                                                               |
#===============================================================================|

def createXYBoard(xyBoard):
    for x in range(60):
        xyBoard.append([])
        for y in range(15):
            if random.randint(1,2) == 1:
                xyBoard[x].append("~")
            else:
                xyBoard[x].append("`")

#===============================================================================|
#                                                                               |
# function printBoard(xyBoard)                                                  |
#   this function is used to print out the board in a nice ascii style layout.  |
#   we do this by using variables to do a while loop through the xyBoard and    |
#   adding each rows charachter to a new list called pBoard (printing Board)    |
#   afterwich we create and print the string for the tens column and then print |
#   the ones collum. after that we print from a range the horizontal lines from |
#   the pBoard                                                                  |
# arguments:                                                                    |
#   xyBoard is the list of lists used to create the list that will print the    |
#       board for feedback to the player.                                       |
# returns:                                                                      |
#   nothing :D                                                                  |
#                                                                               |
#===============================================================================|

def printBoard(xyBoard):
    y = 0
    pBoard = ["","","","","","","","","","","","","","",""]
    while y < len(xyBoard[0]):
        x = 0
        while x < len(xyBoard):
            pBoard[y] += xyBoard[x][y]
            x += 1
        y += 1
    tens = "    "
    for i in range(1,6):
        tens += "         " + str(i)
    print tens
    print "   " + ("0123456789"*6)
    for i in range(15):
        if i < 10:
            isExtraSpace = " "
        else:
            isExtraSpace = ""
        print " %s%s%s %s" %(i,isExtraSpace,pBoard[i],i)
    print "   " + ("0123456789"*6)
    print tens

#===============================================================================|
#                                                                               |
# function again()                                                              |
#   function for getting if the player wants to play again                      |
#   arguments:                                                                  |
#       none                                                                    |
#   returns:                                                                    |
#       true or false depending on player input                                 |
#   *special note*                                                              |
#       even though you don't need the "is True" part of:                       |
#           if again.lower().startswith("y" is True and len(again) < 4          |
#       i left it there for easier reading by the coder                         |
#                                                                               |
#===============================================================================|

def goAgain():
    again = raw_input("Play again? (yes or no)>").lower()
    if again.startswith("y") is True and len(again) < 4:
        return True
    else:
        return False

#===============================================================================|
#                                                                               |
# function playerMove ( xyBoard , chests , sonar )                              |
#   function for getting the players move and then placing it on the board with |
#   the number of the closest chest.                                            |
# arguments:                                                                    |
#   xyBoard is the game board that tells the player whats goin on               |
#   chests is the coordinates of where the chests are                           |
#   sonar is the number of devices that you have                                |
#                                                                               |
#===============================================================================|

def playerMove(xyBoard,chests,sonar,moveList):
    print """Pick the place that you want to place your sonar device. Use the format:
X Y ,where X is a number between 0 and 59 and Y is a number between 0 and 14."""
    move = raw_input("Where would you like to place your sonar device?>").split(" ")
    if move == "quit":
        print "Thanks for looking, Captain."
        sys.exit()
    if not validMove(move):
        print "You must have a number followed by a space then another number..."
        printBoard(xyBoard)
        playerMove(xyBoard,chests,sonar,moveList)
    move[0],move[1] = int(move[0]),int(move[1])
    numericSonar(xyBoard,chests,move,moveList)
    sonar -= 1
    return sonar

#===============================================================================|
#                                                                               |
# function getChests ( xyBoard , chests )                                       |
#   function designed to randomly place three chests into the chests list       |
# arguments:                                                                    |
#   xyBoard is the list that contains what the board looks like. Chests must be |
#       within the limits of this board                                         |
#   chests is the list that contains the coordinates of the chests. since it is |
#       a list and lists are considered global by python i can modify the       |
#       argument chests to modify chests as a whole                             |
#                                                                               |
#===============================================================================|
    
def getChests(xyBoard,chests):#randomly gets the coordinates for three chests
    chests.remove[1]
    while len(chests) < 3:
        xChest = random.randint( 0 , len ( xyBoard ) )
        yChest = random.randint( 0 , len ( xyBoard [0] ) )
        chests.append( [xChest,yChest,0] )

#===============================================================================|
#                                                                               |
# function validMove ( move )                                                   |
#   this function is desik if the players move is something that    |
#   falls withing the border of the game board                                  |
# arguments:                                                                    |
#   move is the players move created from playersMove function                  |
#                                                                               |
#===============================================================================|

def validMove(move):
    if (move[0].isdigit() and move[1].isdigit()) and (int(move[0]) < 60 and int(move[1]) < 15):
        return True
    else:
        return False

#===============================================================================|
#                                                                               |
# gets the info on the droped sonar and gives it the appropriate number
#                                                                               |
#===============================================================================|

def numericSonar(xyBoard,chests,move,moveList):
    moveList.append(move)
    holder = []
    # this partchecks if your move
    for check in chests:
        if check == move:
            chests.remove(move)
            xyBoard[ move[0] ] [ move[1] ] = 0
            print "You found a chest! %s more to go!" %(len(chests))
            updateChests(xyBoard,chests,moveList)
    while len(holder) < len(chests):
        # this sets up a list to check the difference between the move and chest
        # coordinates
        cX = chests[len(holder)][0]
        cY = chests[len(holder)][1]
        holder.append ( [ abs(cX - move[0]), abs(cY - move[1]) ] )
    if min(min(holder) ) < 10:
        chests[chests.index(min(holder)][2] += 1
        xyBoard[move[0]][move[1]] = min(min(holder))
        if chests[chests.index(min(holder)][2] == 3:
            temp = chests[chests.index(min(holder))]
            chests.remove(temp)
            updateChests(xyBoard,chests,moveList)
            print "You found a chest! %s more to go!" %(len(chests))
    elif min(min(holder) ) >= 10:
        print "Sorry Captain, no chests in range..."
        xyBoard[move[0]][move[1]] = 0

#===============================================================================|
#                                                                               |
#
#                                                                               |
#===============================================================================|

def updateChests(xyBoard,chests,moveList):

#===============================================================================|
#                                                                               |
#
#                                                                               |
#===============================================================================|

again = True
if raw_input("Sonar!\nSee instructions? (yes or no)>").lower().startswith("y") is True:
    print """
Sonar is a game where you as a Sea Captain try to find three sunken chests. You
get sixteen sonar devices that can find a chest up to 90 meters away (one block
is 10 meters). In the following example where the fours are is fourty meters
away from the sonar device (which is represented here as a d) and the twos are
twenty meters away.

444444444
4       4
4 22222 4
4 2   2 4
4 2 d 2 4
4 2   2 4
4 22222 4
4       4
444444444

Press enter to continue...
"""
    input()
    print"""
If there is a chest within range of the sonar device then it will be represented
by a number. In the following example there is a chest (c is used to represent
the chest here) fourty meters away from the sonar device so instead of a 0 (no
chests within range is shown as a zero)there is a four where you dropped the
sonar device.

444444444
4       4
c 22222 4
4 2   2 4
4 2 4 2 4
4 2   2 4
4 22222 4
4       4
444444444

Press enter to coninue...
"""
    input()
    print"""
You can quit anytime there is input prompt by typing quit. Good luck captain.
"""
moveList = []
while again is True:
    sonarDevices = 16
    chests = [1]
    board = []
    createXYBoard(board)
    while sonarDevices > 0 and len(chests) > 0:
        printBoard(board)
        getChests(board,chests)
        sonarDevices = playerMove(board,chests,sonarDevices,moveList)
    if len(chests) == 0:
        print "Congratulations on finding all the chests, captain!"
    elif sonarDevices == 0 and len(chests) > 0:
        print "Sorry, Captain. We have to go back to shore and get more sonar devices. We failed."
    again = goAgain()
sys.exit()
