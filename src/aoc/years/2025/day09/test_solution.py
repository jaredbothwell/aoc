from aoc.utils.testing import test_solve

from .solution import solve

test_input: list[tuple[str, int, int]] = [
    (
        """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""",
        50,
        24,
    )
]


def test_solution():
    test_solve(solve, test_input)
