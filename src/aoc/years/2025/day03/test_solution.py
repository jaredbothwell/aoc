from aoc.utils.testing import test_solve

from .solution import solve

test_input: list[tuple[str, int, int]] = [
    (
        """987654321111111
811111111111119
234234234234278
818181911112111""",
        357,
        3121910778619,
    )
]


def test_solution():
    test_solve(solve, test_input)
