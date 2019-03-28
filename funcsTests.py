#Project 3 - Word Puzzle
#
#Names: Michael Haneman, Rohith Dara
#Instructor: S. Einakian
#Section: 01

import unittest
from funcs import *


class TestCases(unittest.TestCase):

    def test_checkForward(self):
        puzzle = "x" * 96 + "asdf"
        self.assertEqual(checkForward("asdf", puzzle), True)
        self.assertEqual(checkForward("aaaa", puzzle), False)
        pass

    def test_checkBackward(self):
        puzzle = "x" * 96 + "fdsa"
        self.assertEqual(checkBackward("asdf", puzzle), True)
        self.assertEqual(checkBackward("fdsa", puzzle), False)
        pass

    def test_checkDown(self):
        puzzle = "a" + "x" * 9 + "s" + "x" * 9 + "d" + "x" * 9 + "f" + "x" * 69
        self.assertEqual(checkDown("asdf", puzzle), True)
        self.assertEqual(checkDown("fdsa", puzzle), False)
        pass

    def test_checkUp(self):
        puzzle = "f" + "x" * 9 + "d" + "x" * 9 + "s" + "x" * 9 + "a" + "x" * 69
        self.assertEqual(checkUp("asdf", puzzle), True)
        self.assertEqual(checkUp("fdsa", puzzle), False)
        pass




if __name__ == '__main__':
    unittest.main()
