from dataclasses import dataclass
from functools import reduce
from itertools import groupby, zip_longest
from operator import mul, add
from typing import Callable


@dataclass
class Problem:
    nums: list[int]
    op: Callable[[int, int], int]


operator_map = {"+": add, "*": mul}


def compute_problems(problems: list[Problem]) -> int:
    return sum(reduce(p.op, p.nums) for p in problems)


def part1(
    lines: list[str], operators: list[Callable[[int, int], int]]
) -> list[Problem]:
    numbers_grid = [list(map(int, line.split())) for line in lines]
    problems = [
        Problem(
            nums=[numbers_grid[row][col] for row in range(len(numbers_grid))],
            op=operators[col],
        )
        for col in range(len(numbers_grid[0]))
    ]
    return problems


def part2(
    lines: list[str], operators: list[Callable[[int, int], int]]
) -> list[Problem]:
    columns = ["".join(x).strip() for x in zip_longest(*lines, fillvalue=" ")]
    groups = [
        list(group) for key, group in groupby(columns, key=lambda x: x == "") if not key
    ]
    problems = [
        Problem(nums=list(map(int, group)), op=operators[i])
        for i, group in enumerate(groups)
    ]
    return problems


def parse_input(input_data: str) -> tuple[list[str], list[Callable[[int, int], int]]]:
    lines = input_data.splitlines()
    operators = [operator_map[op] for op in lines[-1].split()]
    return lines[:-1], operators


def solve(input_data: str) -> tuple[int, int]:
    number_lines, operators = parse_input(input_data)
    part1_data = part1(number_lines, operators)
    part2_data = part2(number_lines, operators)
    return compute_problems(part1_data), compute_problems(part2_data)
