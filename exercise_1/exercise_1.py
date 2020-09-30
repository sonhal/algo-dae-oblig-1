from exercise_1.trie import Trie
from exercise_1.trie_file import TrieFile


class Exercise1:
    """Undestands solving Oblig"""

    def __init__(self, file):
        self._input = TrieFile(file)
        self._trie = Trie()
        self._rapport = Exercise1Rapport()
        for word in self._input.words():
            self._trie.insert(word)
            self._rapport .register_insert(self._trie, word)
        for key in self._input.keys():
            result = self._trie.search(key)
            self._rapport .register_search(key, result)

    def write_to_output(self, out_file):
        self._rapport.write(out_file)


class Exercise1Rapport:

    def __init__(self):
        self._word_lines = []
        self._search_lines = []

    def register_insert(self, trie_after_insert: Trie, word: str):
        self._word_lines.append(f"{word}:{str(trie_after_insert)}")

    def register_search(self, key, result: bool):
        self._search_lines.append(f"{key} {'YES' if result else 'NO'}")

    def build(self):
        return self._word_lines + self._search_lines

    def write(self, file):
        with open(file, "w") as file:
            for line in self.build():
                file.write(line + "\n")

