"""
This program is a game of tic tac toe.
to be played hot seat or against an ai
"""
#-------------------------------------------------------------------------------
#
#Imports
#
#-------------------------------------------------------------------------------

import os
import random

#-------------------------------------------------------------------------------
#
# the following function will be used to:
#       - indicate where the peices are on the board
#       - send the computer to the players input
#       - send the copmuter to the ai moves
#       - print victory information
#       - arguments:
#           - turn : says wether its player or computer turn a value of 1 has
#               the computer go. a value of 0 has the player go
#           - grid : says what pieces go where
#           - aiPlay : says wether its player vs player or player vs computer
#               a value of one indicates that it is player vs computer
#           - vicForO : contains the info if the O piece has won or not
#               a value of one indicates that O has won unless vicForX is also 1
#               which indicates a tie
#           - vicForX : contains the info if the X piece has won or not
#               a value of one indicates that X has won unless vicForO is also 1
#               which indicates a tie
#           - pPiece : holds the info on what the players game piece is
#           - cPiece : holds the info on what the computers game piece is
#       - returns : nothing
#
#-------------------------------------------------------------------------------

def gameBoard ( turn , grid , aiPlay , vicForO , vicForX , pPiece , cPiece ):
    while vicForO != 1 and vicForX != 1:
        if turn == 2:
            turn = 0
        elif turn == 3:
            turn = 1
        os.system ( "cls" )
        print """   |   |
""","",grid[0],"|",grid[1],"|",grid[2],"""
   |   |
===========
   |   |
""","",grid[3],"|",grid[4],"|",grid[5],"""
   |   |
===========
   |   |
""","",grid[6],"|",grid[7],"|",grid[8],"""
   |   |"""
        if turn == 1 and vicForO != 1 and vicForX != 1:
            """
            this is the area that sends you too the ai move or oposing player move
            """
            if aiPlay == 1:
                #against computer
                grid , vicForO , vicForX = aiMove ( grid , vicForO , vicForX , cPiece )
            else:
                #against another player
                grid , vicForO , vicForX = playerMove ( grid , vicForO, vicForX , cPiece )
            turn = 2
        elif turn == 0 and vicForO != 1 and vicForX != 1:
            """
            this is the area that gets the players move or first persons move
            """
            grid , vicForO , vicForX = playerMove ( grid , vicForO , vicForX , pPiece )
            turn = 3
    os.system ( "cls" )
    print """
   |   |
""","",grid[0],"|",grid[1],"|",grid[2],"""
   |   |
===========
   |   |
""","",grid[3],"|",grid[4],"|",grid[5],"""
   |   |
===========
   |   |
""","",grid[6],"|",grid[7],"|",grid[8],"""
   |   |"""
    """
    prints the victory information for the player(s) to see
    """
    if vicForO == 1 and vicForX != 1:
        if cPiece == "O":
            if aiPlay == 1:
                print "The Computer has won! Better luck next time..."
                os.system ( "cls" )
            else:
                print "Player 2 is the winner! Try harder Player 1..."
                os.system ( "cls" )
        else:
            if aiPlay == 1:
                print "The Player has Won! Good job!"
                os.system ( "cls" )
            else:
                print "Player 1 is the winner! Try harder Player 2..."
                os.system ( "cls" )
    elif vicForO != 1 and vicForX == 1:
        if cPiece == "X":
            if aiPlay == 1:
                print "The Computer has won! Better luck next time..."
                os.system ( "cls" )
            else:
                print "Player 2 is the winner! Try harder Player 1..."
                os.system ( "cls" )
        else:
            if aiPlay == 1:
                print "The Player has Won! Good job!"
                os.system ( "cls" )
            else:
                print "Player 1 is the winner! Try harder Player 2..."
                os.system ( "cls" )
    elif vicForO == 1 and vicForX == 1:
        print "Neither side has won..."
        
#-------------------------------------------------------------------------------
#
# the following function is supposed to:
#       - read the board for conditions to:
#           - place a piece that will earn the ai victory
#           - place a piece that will block the player from victory
#           - randomly place a piece in the corners if they are empty
#           - place a piece in the center if it is empty
#           - randomly place a piece in the sides, top, bottom if they are empty
#           - arguments :
#               - piece : this is the computers piece and is used to determine
#                   what the players piece is
#               - grid : this is the variable that holds the information on
#                   where the pieces X and O are on the game board
#               - vicO : this is the variable that holds the information on
#                   wether or not O has won
#               - vicX : this is the variable that holds the information on
#                   wether or not X has won
#           - returns :
#               - grid : the updated information on where the computer has
#                   decided to place its piece
#               - vicO : the updated information on the victory condition of O
#               - vicX : the updated information on the victory condition of X
#           - calls the victory check function, vicCheck
#
#-------------------------------------------------------------------------------
        
def aiMove ( grid , vicO , vicX , piece ):
    move = 0
    if piece == "O":
        piece2 = "X"
    if piece == "X":
        piece2 = "O"
    while move != 1:
        """
        This loop will check to see if there as a condition that allows for the
        computer to win with this move and then takes that move
        """
        if move != 1:
            counter = 0
            holder = [grid[0:3],grid[3:6],grid[6:9],grid[0:9:4],grid[2:7:2],grid[2:9:3],grid[1:8:3],grid[0:7:3]]
            while counter <= 7:
                if move != 1:
                    a = 0
                    for l in holder[counter]:
                        if l == piece:
                            a += 1
                            print debug[counter]
                    print a
                    if a == 2:
                        for l in holder[counter]:
                            if l != piece and l != piece2:
                                grid[grid.index(l)] = piece
                                move = 1
                counter += 1
        """
        If in the previous move there was no possibility for the computer to
        make a winning move then the computer checks to see if the player can
        make a winning move and trys to block it.
        """
        if move != 1:
            counter = 0
            holder = [grid[0:3],grid[3:6],grid[6:9],grid[0:9:4],grid[2:7:2],grid[2:9:3],grid[1:8:3],grid[0:7:3]]
            while counter <= 7:
                if move != 1:
                    a = 0
                    for l in holder[counter]:
                        if l == piece2:
                            a += 1
                    if a == 2:
                        for l in holder[counter]:
                            if l != piece2:
                                grid[grid.index(l)] = piece
                        move = 1
                counter += 1
        """
        If in the previous two move checks there was no move for the ai to make
        then it checks to see if the corners are empty. If one of them is empty
        then it will randomly choose one of them to place its piece
        """
        if (grid[0] == 1 or grid[2] == 3 or grid[6] == 7 or grid[8] == 9) and move != 1:
            numeral = 800
            while numeral != 1 or numeral != 3 or numeral != 7 or numeral != 9:
                numeral = random.randint ( 1 , 9 )
            grid[grid.index(numeral)] = piece
            move = 1
        """
        If in the previous three move checks there was no available move then 
        the computer checks to see if it can place a piece in the center and
        then places its piece there if it can.
        """
        if grid[4] == 5 and move!= 1:
            grid[4] = piece
            move = 1
        """
        If all else fails, the computer checks the sides and top/bottom for an
        empty place to move. If there is one, then it randomly chooses between
        them and places its piece there
        """
        if (grid[1] == 2 or grid[3] == 4 or grid[5] == 6 or grid[7] == 8) and move != 1:
            numeral =599
            while numeral != 2 or numeral != 4 or numeral != 6 or numeral != 8:
                numeral = random.randint ( 2 , 8 )
            grid[grid.index(numeral)] = piece
            move = 1
    vicO , vicX = vicCheck ( grid , piece )
    return grid , vicO , vicX

#-------------------------------------------------------------------------------
#
# the following function is supposed to:
#       - get the plyers input
#       - replace the indicated number with the players piece
#       - return the info to gameboard function
#       - arguments:
#           - grid : contains the information on where the pieces are in the
#               game board
#           - vicO : contains the information on wether or not O has a victory
#           - vicX : contains the information on wether of not X has a victory
#           - piece : contains the information on the players piece to be placed
#               on the game board
#       - returns:
#           - grid : updated info on the state of the game board
#           - vicO : updated info on victory conditions of O
#           - vicX : updated info on victory conditions of X\
#       - calls the victory check function, vicCheck
#
#-------------------------------------------------------------------------------

def playerMove ( grid , vicO , vicX , piece ):
    place = input ( "Where would you like to place your piece?>" )
    for numeral in grid:
        if numeral == place:
            grid[grid.index(place)] = piece
    vicO , vicX = vicCheck ( grid , piece )
    return grid , vicO , vicX
    
#-------------------------------------------------------------------------------
#
# the following function is supposed to:
#       - check for the victory of x and o
#       - arguments
#           - grid this is the list that will be used to determine the victory
#               conditions of X and O
#           - piece this is the piece that is primarily being checked. this
#               is sent by the computer and player move functions as an x
#               or o and is used to determine the other piece to compare against
#
#-------------------------------------------------------------------------------

def vicCheck ( grid , piece ):
    counter = 0
    vicO = 0
    vicX = 0
    if piece == "O":
        piece2 = "X"
    elif piece == "X":
        piece2 = "O"
    holder = [grid[0:3],grid[3:6],grid[6:9],grid[0:9:4],grid[2:7:2],grid[2:9:3],grid[1:8:3],grid[0:7:3]]
    while counter <= 7:
        a = 0
        b = 0
        for l in holder[counter]:
            if l == piece:
                a += 1
            elif l == piece2:
                b += 1
        if (a >= 3 and piece == "X") or (b >= 3 and piece2 == "X"):
            vicX = 1
        if (a >= 3 and piece == "O") or (b >= 3 and piece2 == "O"):
            vicO = 1
        counter += 1
    a = 0
    for l in grid:
        if l == "X" or l == "O":
            a += 1
        if a >= 7:
            vicX = 1
            vicO = 1
    return vicO , vicX

#-------------------------------------------------------------------------------
#
# the following is the control loop of the game. it contains:
#       - defining main variables
#       - asking if player wants to play again
#       - reseting game logic
#
#-------------------------------------------------------------------------------

vicO = 0
vicX = 0
turn = 50
again = 1
PIECECHECK = "x X".split()
AIPLAYCHECK = "y Y yes Yes YES YeS YEs".split()
"""
this will be the while loop that keeps the game playing
"""
while again == 1:
    grid = [7,8,9,4,5,6,1,2,3]
    os.system ( "cls" )
    aiPlay = raw_input ( "Play against AI? (Yes or No)>" )
    for a in AIPLAYCHECK:
        if a == aiPlay:
            aiPlay = 1
            break
    playerPiece = raw_input ( "Play as : X or O >" )
    for a in PIECECHECK:
        if a == playerPiece:
            pPiece = "X"
            cPiece = "O"
            break
        elif a != playerPiece:
            pPiece = "O"
            cPiece = "X"
            break
    turn = random.randint ( 0 , 1 )
    if turn == 1:
        if aiPlay == 1:
            print "The Computer goes first..."
            raw_input("Press Enter to continue")
        else:
            print "Player Two goes first..."
            raw_input("Press Enter to continue")
    else:
        print "Player goes first..."
        raw_input("Press Enter to continue")
    gameBoard (  turn , grid , aiPlay , vicO , vicX , pPiece , cPiece )
    os.system ( "cls" )
    #uses again as the raw_input variable so that if it doesnt say yes
    #the while loop will definetly end
    again = raw_input ( "Again? (Yes or No)>" )
    for a in AIPLAYCHECK:
        if a == again:
            again = 1
            break
quit()
