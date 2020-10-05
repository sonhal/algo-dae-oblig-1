from typing import List


class Trie:
    """Understands traversals of words as linked character Nodes"""

    def __init__(self):
        self._root = Node.root()

    def insert(self, word: str):
        self._root.insert(word.lower())

    def search(self, key: str):
        key_list = [char for char in key.lower()]
        current = self._root
        for _ in range(0, len(key)):
            current = current._children.get(key_list.pop(0))
            if current is None:
                return False
        return current is not None and current.is_end_of_word

    def __str__(self):
        result = []
        current = self._root
        stack = []
        while True:
            if isinstance(current, str):
                result.append(current)
            else:
                stack += self._create_stack_elements(current, list(current._children.values()))
                result.append(current._value)
            try:
                current = stack.pop()
            except IndexError:
                break
        return "".join(result)

    @staticmethod
    def _create_stack_elements(node, children: List["Node"]):
        if len(children) > 1 or node.is_end_of_word:
            result = []
            for child in reversed(children):
                result.append(")")
                result.append(child)
                result.append("(")
            return result
        return children


class Node:

    def __init__(self, char: str, is_end_of_word: bool = False):
        if len(char) > 1:
            raise ValueError(f"char is invalid: <{char}>")
        self._value = char
        self._children = {}
        self.is_end_of_word = is_end_of_word

    def insert(self, word: str):
        if self._child(word[0]) is None:
            self._make_child(word[0], len(word) == 1)
        elif len(word) == 1:
            self._child(word[0]).is_end_of_word = True
        if len(word) > 1:
            self._child(word[0]).insert(word[1:])

    def _child(self, char: str) -> "Node":
        if len(char) > 1:
            raise ValueError(f"char is invalid: <{char}>")
        return self._children.get(char)

    def _make_child(self, char: str, is_end_of_word: bool):
        if len(char) > 1:
            raise ValueError(f"char is invalid: <{char}>")
        self._children[char] = Node(char, is_end_of_word)

    def __str__(self):
        return self._value

    def __len__(self):
        return len(self._children)

    @classmethod
    def root(cls):
        return Node("", True)
