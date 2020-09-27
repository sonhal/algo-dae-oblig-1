import unittest
from pathlib import Path

from oblig_1.exercise_1.Tries import Trie
from oblig_1.exercise_1.visitor import PrefixVisitor

TEST_DATA = Path(__file__).absolute()


TEST_DATA_STR = """
"""

inserts = ["internet", "interview", "inter", "internally", "web", "world"]
lookups = ["internet"]


class TestTries(unittest.TestCase):

    def test_end_2_end(self):
        trie = Trie()
        for key in inserts:
            trie.insert(key)
            prefix_visitor = PrefixVisitor()
            trie.accept(prefix_visitor)
            print(prefix_visitor)

    def test_first_char_split(self):
        keys = ["internet","web", "world"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
            prefix_visitor = PrefixVisitor()
            trie.accept(prefix_visitor)
            print(prefix_visitor)
