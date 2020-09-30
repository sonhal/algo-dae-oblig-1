import unittest
from pathlib import Path

from exercise_1.exercise_1 import Exercise1Rapport, Exercise1
from exercise_1.trie import Trie

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
            print(trie)

    def test_first_char_split(self):
        keys = ["internet","web", "world"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
            print(trie)

    def test_search_same_word(self):
        keys = ["internet"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertTrue(trie.search(keys[0]))

    def test_sub_word(self):
        keys = ["internet", "interview", "inter"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertTrue(trie.search(keys[2]))

    def test_not_word(self):
        keys = ["internet", "interview", "inter"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertFalse(trie.search("cool"))

    def test_almost_right_search(self):
        keys = ["internet", "interview", "inter", "internally", "web", "world"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        key = "wel"
        self.assertFalse(trie.search(key))

    def test_prefix_visitor_single_word(self):
        keys = ["internet"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(internet)", str(trie))

    def test_prefix_visitor_distinct_words(self):
        keys = ["internet", "web", "key"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(internet)(web)(key)", str(trie))

    def test_sub_and_super_word(self):
        keys = ["inter", "internet"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(inter(net))", str(trie))

    def test_prefix_visitor(self):
        keys = ["internet", "interview", "inter", "internally", "web", "world", "key", "keys"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(inter(n(et)(ally))(view))(w(eb)(orld))(key(s))", str(trie))


    def test_to_str(self):
        keys = ["internet"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(internet)", str(trie))


    def test_to_str(self):
        keys = ["internet", "key", "bollocks"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(internet)(key)(bollocks)", str(trie))

    def test_prefix_visitor(self):
        keys = ["internet", "interview", "inter", "internally", "web", "world", "key", "keys"]
        trie = Trie()
        for key in keys:
            trie.insert(key)
        self.assertEqual("(inter(n(et)(ally))(view))(w(eb)(orld))(key(s))", str(trie))

    def test_rapport(self):
        keys = ["internet", "interview", "inter", "internally", "web", "world", "key", "keys"]
        searches = ["inter", "internet", "web", "key", "waldo", "w", "i", "cool"]
        trie = Trie()
        rap = Exercise1Rapport()
        for key in keys:
            trie.insert(key)
            rap.register_insert(trie, key)
        for key in searches:
            result = trie.search(key)
            rap.register_search(key, result)
        result = rap.build()
        print(result)

    def test_e2e(self):
        file = "test_data_1.txt"
        Exercise1(file).write_to_output("test_out.txt")
