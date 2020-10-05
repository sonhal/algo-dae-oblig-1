import unittest

from exercise_2.sum_of_selections import SumOfSelections


class TestSumOfSelection(unittest.TestCase):

    def test_find_satisfying_selection(self):
        selection = [2, 1, 3, 4]
        sos = SumOfSelections(selection)
        result = sos.satisfies(0)
        self.assertSequenceEqual([], result.satisfies_set)
        result = sos.satisfies(1)
        self.assertSequenceEqual([1], result.satisfies_set)
        result = sos.satisfies(5)
        self.assertSequenceEqual([1, 4], result.satisfies_set)
        result = sos.satisfies(6)
        self.assertSequenceEqual([2, 4], result.satisfies_set)
        result = sos.satisfies(10)
        self.assertSequenceEqual([1, 2, 3, 4], result.satisfies_set)

    def test_regresion(self):
        selection = [2, 5, 6, 3, 10]
        sos = SumOfSelections(selection)
        result = sos.satisfies(4)
        self.assertSequenceEqual([], result.satisfies_set)
        self.assertFalse(result.satisfies)

    def test_wont_find_satisfying_selection(self):
        selection = [1, 2, 5]
        sos = SumOfSelections(selection)
        result = sos.satisfies(4)
        self.assertSequenceEqual([], result.satisfies_set)


