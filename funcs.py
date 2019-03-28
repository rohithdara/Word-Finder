# Project 3
# 
# Name: Michael Haneman, Rohith Dara
# Instructor: S. Einakian
# Section: 01
'''
Some of the suggested functions are shown bellow.
You can create as many functions as you need. 
You can even ignore the suggested functions.
But you are not allow to write the whole project in One Function!
'''

def printPuzzle(puzzle):
    for i in range(0,100,10):
        print(puzzle[i:i+10])

#Ask the user for the puzzle
#Save the puzzle with the return function

#gets input for puzzle
#str->none
def getPuzzle():
     return input()

def getWords():
    return input()


#Pseudocode for checkForward:
#Create an empty list named rows
#Divide the puzzle into a 10x10 grid by creating a new line per increment of 10
#Traverse each row based on the length of the given word
#Check every slice of the list that is the same length as the word to see if they are equal
#If they are equal, print the location of the first letter of the word
#If they are not equal, return False

#Checks the forward direction for the given puzzle to see if any of the specified words are present
#str,str->bool
def checkForward(val, puzzle):
    rows = []
    for i in range(0,100,10):
        rows.append(puzzle[i:i+10])

    for i in range(len(rows)):
        for j in range(10 - len(val) + 1):
            if rows[i][j:j+len(val)] == val:
                print(str(val) + ": " + "(FORWARD)" + " row: " + str(i) + " column: " + str(j))
                return True
    return False

#Pseudocode for checkBacward:
#Reverse the letters of the given word
#Create an empty list named rows
#Divide the puzzle into a 10x10 grid by creating a new line per increment of -10 -- this will recreate the puzzle into a backward 10x10 grid
#Traverse each row based on the length of the given word
#Check every slice of the list that is the same length as the word to see if they are equal
#If they are equal, print the location of the first letter of the word
#If they are not equal, return false

#Checks the backward direction for the given puzzle to see if any of the specified words are present
#str,str->bool
def checkBackward(val, puzzle):
    bval = val[::-1]
    rows = []
    for i in range(90, 0, -10):
        rows.insert(0,puzzle[i : i + 10])


    for i in range(len(rows)):
        for j in range(10 - len(bval) + 1):
            if rows[i][j:j+len(bval)] == bval:
                print(str(val) + ": " + "(BACKWARD)" + " row: " + str(i + 1) + " column: " + str(j + len(bval) - 1))
                return True
    return False

#Pseudocode for checkUp:
#Create an empty list named columns
#Divide the puzzle into a 10x10 grid by creating a new line for every value in a column starting from the bottom to the top
#Traverse each column based on the length of the given word
#Check every slice of the list that is the same length as the word to see if they are equal
#If they are equal, print the location of the first letter of the word
#If they are not equal, return false

#Checks the upward direction for the given puzzle to see if any of the specified words are present
#str,str->bool
def checkUp(val, puzzle):
    columns = []
    for i in range(9,-1,-1):
        result = ""
        for j in range(9,-1,-1):
            result += puzzle[(j * 10) + i]
        columns.append(result)

    for i in range(len(columns)):
        for j in range(10 - len(val) + 1):

            if columns[i][j:j+len(val)] == val:
                print(str(val) + ": " + "(UP)" + " row: " + str(9-j) + " column: " + str(9-i))
                return True
    return False

#Pseudocode for checkDown:
#Create an empty list named columns
#Divide the puzzle into a 10x10 grid by creating a new line for every value in a column starting from the top to the bottom
#Traverse each column based on the length of the given word
#Check every slice of the list that is the same length as the word to see if they are equal
#If they are equal, print the location of the first letter of the word
#If they are not equal, return false

#Checks the downward direction for the given puzzle to see if any of the specified words are present
#str,str->bool
def checkDown(val, puzzle):
    columns = []
    for i in range(10):
        result = ""
        for j in range(10):
            result += puzzle[(j * 10) + i]
        columns.append(result)

    for i in range(len(columns)):
        for j in range(10 - len(val) + 1):

            if columns[i][j:j + len(val)] == val:
                print(str(val) + ": " + "(DOWN)" + " row: " + str(j) + " column: " + str(i))
                return True
    return False




