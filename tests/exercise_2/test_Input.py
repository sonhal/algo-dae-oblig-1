import os
import tempfile
from pathlib import Path
from unittest import TestCase

from exercise_2.input import Input, Problem

TEST_DATA = """
5 14 1 5 6 3 10
5 4 2 5 6 3 10 
"""


class TestInput(TestCase):

    def setUp(self):
        self.testfilename = tempfile.mkstemp()[1]
        with open(self.testfilename, "w") as file:
            file.write(TEST_DATA)
        self.testfile = open(self.testfilename, "r")

    def tearDown(self):
        self.testfile.close()
        os.remove(self.testfilename)

    def test_instances(self):
        e_input = Input(self.testfilename)
        self.assertEqual([Problem(14, [1, 5, 6, 3, 10]), Problem(4, [2, 5, 6, 3, 10])], e_input.instances())
