#hangman
import random
#import os
import time

#this function takes the wordlist and gets a random word from it as well as 
making a list that has blank spaces for each letter
def getWord(wordList,wrongLetters,hangmanAscii,rightLetters,secretWord):
    randomNumber = random.randint(0, len(wordList) -1)
    chosenWord = wordList[randomNumber]
    rightLetters = []
    for numLetters in chosenWord:
        rightLetters.append(" _")
    gameDisplay(wrongLetters,hangmanAscii,rightLetters,chosenWord)

#this function displayes all the information from player input and such.
def gameDisplay(wrongLetters,hangmanAscii,rightLetters,secretWord,wordList):
    print "You have begun Animal Hangman. This Hangman contains only animal names."
    print "All letters are lowercase. You can only get it wrong six times, so be careful."
    print "There are Fourty-Two animals to guess!"
    time.sleep(8)
    wordCheck = "".join(rightLetters)
    while len(wrongLetters) <= 6 and wordCheck != secretWord:
        #os.system("cls")
        #prints the ascii art for the hangman
        print hangmanAscii[len(wrongLetters)]
        #prints the letter information on number of letters on one line
        for l in rightLetters:
            print l,
        #prints the letters you have guessed on one line
        print "\nYou have guessed: \n"
        for w in wrongLetters:
            print w,
        wrongLetters, rightLetters = getGuess(wrongLetters,rightLetters,secretWord)
        wordCheck = "".join(rightLetters)
    if wordCheck == secretWord:
        #congratulates correct guess
        #os.system("cls")
        print "You guessed right! The secret word was ", secretWord
        time.sleep(4)
        again(wrongLetters,hangmanAscii,rightLetters,secretWord,wordList)
    else:
        #chastises inccorect guess
        #os.system("cls")
        print "You didnt guess the word. The secret word was ", secretWord
        time.sleep(4)
        again(wrongLetters,hangmanAscii,rightLetters,secretWord,wordList)

#the computations happen in this function. it gets players guess as well as
#replacing blanks with a correct guessed letter and adding wrong letters to
#list of wrong letters.
def getGuess(wrongLetters,rightLetters,secretWord):
    playerInput = "moreThanOne"
    #using the above variable to make sure that only one letter is guessed at a time
    while len(playerInput) != 1:
        playerInput = raw_input("\nGuess a letter (Guess only one letter at a time).>")
        str(playerInput)
    str(playerInput)
    a = 0
    wrong = 0
    for letters in secretWord:
        if playerInput == letters:
            #gets rid of the blank space
            del rightLetters[a] 
            #adds correct letter in the place of a blank space
            rightLetters.insert(a , playerInput) 
        else:
            wrong += 1
        a += 1
    if wrong == len(secretWord):
        #Appends wrong letter to the wrongLetters list
        wrongLetters.append(playerInput) 
    return wrongLetters, rightLetters

#function for finding out if the player wants to play again
def again(wrongLetters,hangmanAscii,rightLetters,secretWord,wordList):
    goAgain = raw_input("Go again? (1.Yes 2.No)>")
    possible = [1,"yes","Yes","Y","y","YES","1"]
    for p in possible:
        if goAgain == p:
            #os.system("cls")
            getWord (wordList,wrongLetters,hangmanAscii,rightLetters,secretWord)
        else:
            #os.system("cls")
            quit()
#ascii art to display wrong guess progress
hangmanAscii = ["""

  +===+
  |   |
      |
      |
      |
      |
      |
+=======+""","""

  +===+
  |   |
  0   |
      |
      |
      |
      |
+=======+""","""

  +===+
  |   |
  0   |
  |   |
      |
      |
      |
+=======+""","""

  +===+
  |   |
  0   |
 /|   |
      |
      |
      |
+=======+""","""

  +===+
  |   |
  0   |
 /|\  |
      |
      |
      |
+=======+""","""

  +===+
  |   |
  0   |
 /|\  |
 /    |
      |
      |
+======+""","""

  +===+
  |   |
  0   |
 /|\  |
 / \  |
      |
      |
+=======+"""]

#this is the set of words that the player gets to guess on
wordList = ["ant","ardvark","bear","bull","blueberry","anteater","grizzly","mongoose","goose","horse","bovine","cayote","wolf","lamb","ewe","chicken","rooster","cow","dog","cat","feline","lynx","zebra","bison","cougar","lion","tiger","elephant","sloth","koala","kangaroo","aligator","crocodile","cheetah","fox","orangutang","gorilla","chimpanzee","lemur","mosquito","tarantula","seal"]
secretWord = "" 
rightLetters = []
wrongLetters = []
#starts game by calling the random word getter
getWord (wordList,wrongLetters,hangmanAscii,rightLetters,secretWord)