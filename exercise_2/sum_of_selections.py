from collections.abc import Sequence
from typing import List


class Table(Sequence):

    def __init__(self, T, K):
        self._T = T  # sequence length
        self._S = K  # sum
        self._U = [Table.Row(self._T[i], K, True if i == 0 else False) for i in range(0, len(self._T))]

    def __getitem__(self, i: int):
        return self._U[i]

    def satisfying(self):
        if not self._U[-1][-1]:
            return []
        else:
            visitor = Table.SelectionBuilderVisitor()
            self._U[-1][-1].accept(visitor)
            return visitor.result()

    def __len__(self) -> int:
        return len(self._U)

    def __str__(self):
        return "\n".join([str(s) for s in self._U])

    # Internal Classes --------------------------------------------------

    class Node:

        def __init__(self, value, j, sequence, value_parent=None):
            self._value = value
            self._j = j
            self._seq_parent = sequence
            self._value_parent = value_parent

        def accept(self, visitor):
            if self._value is False:
                return
            if self._value_parent is not None:
                if self._value_parent._j != self._j:
                    visitor.visit(self._seq_parent._col_val)
                self._value_parent.accept(visitor)
            elif self._j != 0:
                visitor.visit(self._seq_parent._col_val)

        def __str__(self):
            return str(self._value)

        def __repr__(self):
            return str(self)

        def __bool__(self):
            return bool(self._value)

    class Row:

        def __init__(self, value, K, first: bool = False):
            self._col_val = value
            self._sequence = [Table.Node(True if j == 0 or (first is True and j == value) else None, j, self) for j in range(0, K + 1)]

        def __setitem__(self, key, value: "TableSequence"):
            if not isinstance(value, Table.Node):
                return ValueError(f"value in sequence: {value} is not a Node")
            self._sequence[key] = Table.Node(value._value, key, self, value)

        def __getitem__(self, i: int):
            return self._sequence[i]

        def __len__(self):
            return len(self._sequence)

        def __str__(self):
            return f"{self._col_val}:{self._sequence}"

        def accept(self, visitor):
            if len(self._sequence) < 1:
                raise ValueError("sequence is empty")
            self._sequence[-1].accept(visitor)

    class SelectionBuilderVisitor:

        def __init__(self):
            self._sat_seq = []  # satisfying sequence of values

        def visit(self, value):
            self._sat_seq.append(value)

        def result(self):
            return self._sat_seq


class SumOfSelections:

    def __init__(self, selection: List[int]):
        self._T = sorted(selection)
        self._original_selection = selection

    def satisfies(self, K: int):

        if self._guard(K) is not None:
            return self._guard(K)

        U = Table(self._T, K)
        for i in range(1, len(self._T)):
            for j in range(1, K + 1):
                U[i][j] = U[i - 1][j] if j < self._T[i] else U[i - 1][j - self._T[i]] or U[i - 1][j]

        if U[len(self._T) - 1][-1]:
            return Result(K, self._original_selection, True, sorted(U.satisfying()))

        return Result.false(K, self._original_selection)

    def _guard(self, K):
        if K > sum(self._T):
            return Result.false(K, self._original_selection)
        if K > 0 and len(self._T) == 0:
            return Result.false(K, self._original_selection)
        if K == 0:
            return Result(K, self._original_selection, True, [])
        return None


class Result:

    def __init__(self, K: int, selection: list, satisfies: bool, satisfies_set: list):
        self.K = K
        self.selection = selection
        self.satisfies = satisfies
        self.satisfies_set = satisfies_set

    @classmethod
    def false(cls, K, selection):
        return cls(K, selection, False, [])

    def __bool__(self):
        return bool(self.satisfies)

