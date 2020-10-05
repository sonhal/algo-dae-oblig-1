from dataclasses import dataclass
from pathlib import Path
from typing import List


class Input:

    def __init__(self, file):
        self._file = Path(file)
        if not self._file.exists():
            raise ValueError("no such file")
        self._instances = []

    def instances(self) -> List["Problem"]:
        if len(self._instances) == 0:
            with open(self._file, "r") as file:
                for line in file.readlines():
                    self._parse_instance(line)
        return self._instances

    def _parse_instance(self, line: str):
        elements = line.lstrip().rstrip().split(" ")
        if len(elements) > 2:
            assert len(elements) == int(elements[0]) + 2
            self._instances.append(Problem(int(elements[1]), [int(value) for value in elements[2:]]))


@dataclass
class Problem:
    K: int
    selection: list

    def __str__(self):
        return f"{len(self.selection)} {self.K}: {' '.join(str(value) for value in self.selection).rstrip(' ')}"
