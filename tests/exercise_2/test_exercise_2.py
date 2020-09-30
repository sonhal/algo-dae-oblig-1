import unittest

from exercise_2.sum_of_selections import SumofSelections


class Exercise1(unittest.TestCase):

    def test_find_selection(self):
        selection = [1, 2, 3, 4]
        sos = SumofSelections(selection)
        result = sos.find(9)
        self.assertEqual([1, 2, 3], result)

