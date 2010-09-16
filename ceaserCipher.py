# -*- coding: utf-8 -*-
"""
this is a program designed to allow one to do the Ceaser Cipher
the ceaser cipher is simple displacement of a letter to a sut number of letters
in a particular direction.

for instance in a ceaser cipher where the key is 2:
a becomes c
b becomes d
c becomes e
and so on and so forth.
"""

#==============================================================================|
#                                                                              |
#   Imports                                                                    |
#                                                                              |
#==============================================================================|

import sys

#==============================================================================|
#                                                                              |
# function getKey()                                                            |
#   this function is designed to get a key from the user and check if it is a  |
#   valid key or not. It will only allow a valid key to be returned.           |
# arguments:                                                                   |
#   none                                                                       |
# returns:                                                                     |
#   returns the key                                                            |
#                                                                              |
#==============================================================================|

def getKey():
    key = int(raw_input("What is the key to the cipher?>") )
    if key > 0 and key < 27:
        return key
    else:
        print "That is not a valid key..."
        getKey()

#==============================================================================|
#                                                                              |
# function getText()                                                           |
#   simply returns the text that the user whishes to encrypt or decrypt        |
# arguments:                                                                   |
#   none                                                                       |
# returns:                                                                     |
#   returns the input of the user                                              |
#                                                                              |
#==============================================================================|

def getText():
    return raw_input("What text would you like translate?>")

#==============================================================================|
#                                                                              |
# function getChoice()                                                         |
#   this function gets what the user wants to do. it ensures that the choice is|
#   within the scope of the program and enforeces the user to those choices    |
#   alone.                                                                     |
# arguments:                                                                   |
#   none                                                                       |
# returns:                                                                     |
#   returns the users choice                                                   |
#                                                                              |
#==============================================================================|

def getChoice():
    print "Are you decrypting or encrypting?"
    choice = raw_input(">").lower()
    if choice in "decrypting d encrypting e".split():
        return choice
    else:
        print "You must type \"decrypting\" or \"d\" or \"encrypting\" or \"e\"."
        getChoice()

#==============================================================================|
#                                                                              |
#
#                                                                              |
#==============================================================================|

def translateText(key,choice,text):
    trans = ""
    if choice == "decrypting" or choice == "d":
        key = -key
    for letter in text:
        if not letter.isupper() and not letter.islower():
            trans += letter
            continue
        if letter.isupper():
            if ord(letter) >= ord("Z"):
                trans += chr(ord(letter) + (key - 26))
            elif ord(letter) <= ord("A"):
                trans += chr(ord(letter) + (key + 26))
            else:
                trans += chr(ord(letter) + key)
        if letter.islower():
            if ord(letter) >= ord("z"):
                trans += chr(ord(letter) + (key - 26))
            elif ord(letter) <= ord("a"):
                trans += chr(ord(letter) + (key + 26))
            else:
                trans += chr(ord(letter) + key)
    return trans

#==============================================================================|
#                                                                              |
#
#                                                                              |
#==============================================================================|

def goAgain():
    again = raw_input("Again? (yes or no)>").lower()
    if again.startswith("y") and len(again) == 3:
        return True
    else:
        return False

#==============================================================================|
#                                                                              |
#
#                                                                              |
#==============================================================================|

print "The Ceaser Cipher"
again = True
while again == True:
    choice = getChoice()
    text = getText()
    key = getKey()
    translation = translateText(key,choice,text)
    print """
Your translated text is:
%s
Write it down so you remember it...""" %(translation)
    again = goAgain()
sys.exit()
