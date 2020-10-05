from typing import List

from exercise_2.sum_of_selections import Result


class SumOfSelectionsMemoized:

    def __init__(self, selection: List[int]):
        self._T = list(sorted(selection))
        self._original_selection = selection
        self._lookup = {}
        self._solutions = {}

    def satisfies(self, K: int):
        self._lookup = {}
        self._solutions = {key: [] for key in range(0, K + 1)}

        if K == 0:
            return Result(K, self._original_selection, True, [])

        result = self._satisfies(len(self._T) - 1, K)
        if result:
            return Result(K, self._original_selection, result, self._sat_selection(K))
        else:
            return Result.false(K, self._original_selection)

    def _satisfies(self, n: int, K: int):
        if K == 0:
            return True

        if n < 0 or K < 0:
            return False

        key = (n, K)
        if key not in self._lookup:
            is_included = self._satisfies(n - 1, K - self._T[n])
            is_excluded = self._satisfies(n - 1, K)
            self._lookup[key] = is_included or is_excluded
        return self._lookup[key]

    def _sat_selection(self, K):
        cur = self._top_satisfier_for(K)
        result = []
        sum = K
        while True:
            result.append(cur)
            sum = sum - self._T[cur]
            if sum <= 0:
                break
            cur = self._top_satisfier_for(sum)
        return list(sorted(map(lambda i: self._T[i], result)))

    def _top_satisfier_for(self, K):
        return [key[0] for key, value in self._lookup.items() if key[1] == K and value is True][0]