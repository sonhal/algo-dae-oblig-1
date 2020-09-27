from typing import List


class Trie:
    """Understands traversals of words as linked character Nodes"""

    def __init__(self):
        self._root = Node.root()

    def insert(self, key):
        self._root.insert(key)

    def accept(self, visitor):
        self._root.accept(visitor)


class Node:

    def __init__(self, char: str):
        if len(char) > 1:
            raise ValueError(f"char is invalid: <{char}>")
        self._value = char
        self._children = {}

    def accept(self, visitor):
        visitor.pre_visit(self)
        for child in self._children.values():
            child.accept(visitor)
            visitor.visit(self)
        visitor.post_visit(self)

    def insert(self, word: str):
        if self._child(word[0]) is None:
            self._make_child(word[0])
        if len(word) > 1:
            self._child(word[0]).insert(word[1:])

    def is_root(self):
        return True if self._value == "" else False

    def _child(self, char: str):
        if len(char) > 1:
            raise ValueError(f"char is invalid: <{char}>")
        return self._children.get(char)

    def _make_child(self, char: str):
        if len(char) > 1:
            raise ValueError(f"char is invalid: <{char}>")
        self._children[char] = Node(char)

    def _num_children(self):
        return len(self._children)

    def __str__(self):
        return self._value

    def __len__(self):
        return len(self._children)

    @classmethod
    def root(cls):
        return Node("")

