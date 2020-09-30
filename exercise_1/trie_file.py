from pathlib import Path


class TrieFile:

    def __init__(self, filename):
        self._filename = Path(filename)
        if not self._filename.exists():
            raise ValueError("no such file")
        self._words = None
        self._keys = None

    def words(self):
        if self._words is None:
            self._words = []
            with open(self._filename, "r") as file:
                word_num = int(file.readline())
                for _ in range(0, word_num):
                    self._words.append(file.readline().rstrip("\n\r")) # clean key of newlines etc
        return self._words

    def keys(self):
        if self._keys is None:
            self._keys = []
            with open(self._filename, "r") as file:
                word_num = int(file.readline().rstrip("\n\r"))
                for _ in range(0, word_num):
                    file.readline()
        return self._words

    @staticmethod
    def _is_number(char):
        try:
            int(char)
            return True
        except ValueError:
            return False



