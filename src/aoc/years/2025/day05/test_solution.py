from aoc.utils.testing import test_solve

from .solution import solve

test_input = [
    (
        """3-5
10-14
16-20
12-18

1
5
8
11
17
32""",
        3,
        14,
    )
]


def test_solution():
    test_solve(solve, test_input)
