from typing import Callable


def assert_part1(actual: int, expected: int, index: int):
    assert actual == expected, (
        f"Expected part1 to be {expected}, but got {actual} at index {index}"
    )


def assert_part2(actual: int, expected: int, index: int):
    assert actual == expected, (
        f"Expected part2 to be {expected}, but got {actual} at index {index}"
    )


def test_solve(
    solve_func: Callable[[str], tuple[int, int]], test_input: list[tuple[str, int, int]]
):
    for index, (input_data, part1_solution, part2_solution) in enumerate(test_input):
        part1, part2 = solve_func(input_data)
        assert_part1(part1, part1_solution, index)
        assert_part2(part2, part2_solution, index)
