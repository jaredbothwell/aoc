from aoc.utils.testing import test_solve

from .solution import solve

test_input: list[tuple[str, int, int]] = [
    (
        """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""",
        3,
        6,
    )
]


def test_solution():
    test_solve(solve, test_input)
