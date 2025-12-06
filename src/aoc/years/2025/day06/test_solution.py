from aoc.utils.testing import test_solve

from .solution import solve

test_input: list[tuple[str, int, int]] = [
    (
"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """,
        4277556,
        3263827,
    ),
]


def test_solution():
    test_solve(solve, test_input)
