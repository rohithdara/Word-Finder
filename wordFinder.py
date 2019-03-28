#Project 3 - Word Puzzle
#
#Names: Michael Haneman, Rohith Dara
#Instructor: S. Einakian
#Section: 01
from funcs import *

#Run the entire word finder function to output the location of the specified words
#->
def main():

   puzzle = getPuzzle()
   words = getWords().split()

   print("Puzzle:" + "\n")
   printPuzzle(puzzle)
   print("")
   for i in range(len(words)):
      cf = checkForward(words[i], puzzle)
      cb = checkBackward(words[i], puzzle)
      cu = checkUp(words[i], puzzle)
      cd = checkDown(words[i], puzzle)
      if cf == False and cb == False and cu == False and cd == False:
         print(str(words[i]) + ": word not found")

if __name__ == "__main__":
   main()
