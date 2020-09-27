from abc import ABC, abstractmethod

from oblig_1.exercise_1.Tries import Node


class Visitor(ABC):

    @abstractmethod
    def pre_visit(self, node: "Node"):
        raise NotImplemented

    @abstractmethod
    def visit(self, node: "Node"):
        raise NotImplemented

    @abstractmethod
    def post_visit(self, node: "Node"):
        raise NotImplemented



class PrefixVisitor(Visitor):

    class Start:

        def __init__(self, parent: "PrefixVisitor"):
            self._parent = parent

        def pre_visit(self, node: Node):
            self._parent._string.append("(")
            self._parent._string.append(node._value)
            return PrefixVisitor.Continue if len(node) > 0 else PrefixVisitor.Start

        def visit(self, node: Node):
            return self.__class__

        def post_visit(self, node: Node):
            if not node.is_root():
                self._parent._string.append(")")
            return PrefixVisitor.Leaf

    class Continue:

        def __init__(self, parent: "PrefixVisitor"):
            self._parent = parent

        def pre_visit(self, node: Node):
            self._parent._string.append(node._value)
            if len(node) > 1:
                self._parent._string.append("(")
            if len(node) == 0:
                self._parent._string.append(")")
                return PrefixVisitor.Leaf
            return PrefixVisitor.Continue

        def visit(self, node: Node):
            return self.__class__

        def post_visit(self, node: Node):
            return PrefixVisitor.Leaf if len(node) == 0 else PrefixVisitor.Start

    class Leaf:

        def __init__(self, parent: "PrefixVisitor"):
            self._parent = parent

        def pre_visit(self, node: Node):
            self._parent._string.append("(")
            self._parent._string.append(node._value)
            return PrefixVisitor.Continue

        def visit(self, node: Node):
            return PrefixVisitor.Start if len(node) > 1 else self.__class__

        def post_visit(self, node: Node):
            return self.__class__

    def __init__(self):
        self._string = []
        self._state = PrefixVisitor.Start(self)

    def pre_visit(self, node: Node):
        self._state = self._state.pre_visit(node)(self)

    def visit(self, node: Node):
        self._state = self._state.visit(node)(self)

    def post_visit(self, node: Node):
        self._state = self._state.post_visit(node)(self)

    def __str__(self):
        return "".join(char for char in self._string)
