import unittest

from exercise_2.sum_of_selection_memoized import SumOfSelectionsMemoized


class TestSumOfSelectionMemoized(unittest.TestCase):

    def test_find_satisfying_selection(self):
        selection = [2, 1, 3, 4]
        sos = SumOfSelectionsMemoized(selection)
        result = sos.satisfies(0)
        self.assertSequenceEqual([], result.satisfies_set)
        result = sos.satisfies(1)
        self.assertSequenceEqual([1], result.satisfies_set)
        result = sos.satisfies(5)
        self.assertEqual(5, sum(result.satisfies_set))
        result = sos.satisfies(6)
        self.assertEqual(6, sum(result.satisfies_set))
        result = sos.satisfies(10)
        self.assertSequenceEqual([1, 2, 3, 4], result.satisfies_set)

    def test_regresion(self):
        selection = [2, 5, 6, 3, 10]
        sos = SumOfSelectionsMemoized(selection)
        result = sos.satisfies(4)
        self.assertSequenceEqual([], result.satisfies_set)
        self.assertFalse(result.satisfies)

    def test_wont_find_satisfying_selection(self):
        selection = [1, 2, 5]
        sos = SumOfSelectionsMemoized(selection)
        result = sos.satisfies(4)
        self.assertSequenceEqual([], result.satisfies_set)
        selection = [1]
        sos = SumOfSelectionsMemoized(selection)
        result = sos.satisfies(4)
        self.assertSequenceEqual([], result.satisfies_set)
        self.assertFalse(result.satisfies)

    def test_finds_empty_selection(self):
        selection = []
        sos = SumOfSelectionsMemoized(selection)
        result = sos.satisfies(0)
        self.assertSequenceEqual([], result.satisfies_set)
        self.assertTrue(result.satisfies)
