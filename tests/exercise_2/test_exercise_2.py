import os
import tempfile
import unittest

from exercise_2.exercise_2 import Exercise2
from exercise_2.sum_of_selections import SumOfSelections

TEST_DATA = """
5 14 1 5 6 3 10
5 4 2 5 6 3 10 
2 10 3 6
"""


class TestExercise2(unittest.TestCase):

    def setUp(self):
        self.testfilename = tempfile.mkstemp()[1]
        with open(self.testfilename, "w") as file:
            file.write(TEST_DATA)
        self.testfile = open(self.testfilename, "r")

    def tearDown(self):
        self.testfile.close()
        os.remove(self.testfilename)

    def test_e2e(self):
        Exercise2(self.testfilename, SumOfSelections).write_to_file("test_exe2.txt")
