from exercise_2.input import Input, Problem
from exercise_2.sum_of_selection_memoized import SumOfSelectionsMemoized
from exercise_2.sum_of_selections import SumOfSelections, Result


class Exercise2:

    def __init__(self, file, strategy):
        e_input = Input(file)
        self._rapport = Exercise2Rapport()
        for inst in e_input.instances():
            result = strategy(inst.selection).satisfies(inst.K)
            self._rapport.register(inst, result)

    def write_to_file(self, filename):
        self._rapport.write(filename)

    @classmethod
    def dynamic(cls, file):
        return Exercise2(file, SumOfSelections)

    @classmethod
    def memoized(cls, file):
        return Exercise2(file, SumOfSelectionsMemoized)


class Exercise2Rapport:

    def __init__(self):
        self._instances = []

    def register(self, problem: Problem, result: Result):
        element = f"INSTANCE {problem}" +\
                  f"\n{'YES' if result.satisfies else 'NO'}"
        if result.satisfies:
            element += f"\nSELECTION {' '.join(self._format_selection(value, problem.selection) for value in result.satisfies_set)}"
        self._instances.append(element)

    def build(self):
        return self._instances

    def write(self, file):
        result = "\n\n".join(self.build()).rstrip().lstrip()
        with open(file, "w") as file:
            file.write(result)

    @staticmethod
    def _format_selection(value, selection: list):
        return f"{value}[{selection.index(value) + 1}]"

    @staticmethod
    def _format_problem_selection(p_selection: list):
        return ""
