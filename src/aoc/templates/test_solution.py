from aoc.utils.testing import test_solve

from .solution import solve

test_input: list[tuple[str, int, int]] = [
    (
        """
""",
        0,
        0,
    )
]


def test_solution():
    test_solve(solve, test_input)
