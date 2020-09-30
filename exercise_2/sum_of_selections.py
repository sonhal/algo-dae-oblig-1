from collections import Sequence
from typing import List, overload


class SubsetTable(Sequence):
    class TableSequence:

        def __setitem__(self, key, value):
            pass  # TODO implement chain of decision

    class FalseSeq(Sequence):

        def __init__(self, S):
            self._S = S

        def __getitem__(self, i: int):
            return False

        def __len__(self) -> int:
            return self._S

    def __init__(self, T, S):
        self._T = T  # sequence length
        self._S = S  # sum
        self._false_seq = SubsetTable.FalseSeq(S)
        self._U = [[True if j == 0 else None for j in range(0, S)] for _ in range(0, len(self._T))]

    def __getitem__(self, i: int):
        if isinstance(i, slice):
            return self._get_slice(i)
        else:
            if i < 0:
                return self._false_seq
            else:
                return self._U[i]

    def _get_slice(self, s: slice):
        return self._U[s]

    def __len__(self) -> int:
        return len(self._U)

    def __str__(self):
        return str(self._U)


class SumofSelections:

    def __init__(self, selection: List[int]):
        self._T = selection

    def find(self, S: int):

        if S > sum(self._T):
            return False
        if S > 0 and len(self._T) == 0:
            return False

        U = SubsetTable(self._T, S)
        # U[n - 1, S - 1] True or False if the value is solvable
        # U[i, j] = U[i - 1, j] if T[i] > S else U[i, j] = U[i - 1, j] or U[i - 1, j - T[i]]
        for i in range(0, len(self._T)):
            for j in range(1, S):
                U[i][j] = U[i - 1][j] if self._T[i] > S else U[i - 1][j] or U[i - 1][j - self._T[i]]

        return U[len(U) - 1][S - 1]
