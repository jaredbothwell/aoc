

from dataclasses import dataclass
from functools import reduce
from itertools import groupby, zip_longest
from operator import mul, add
from typing import Callable


@dataclass
class Problem:
    numbers: list[int]
    operator: Callable[[int, int], int]


def parse_int(s: str) -> int:
    return int(s.strip('+').strip('*').strip())


def compute_problems(problems: list[Problem]) -> int:
    total = 0
    for problem in problems:
        numbers = problem.numbers
        func = problem.operator
        total += reduce(func, numbers)
    return total


def parse_part2(input_data: str) -> list[Problem]:
    lines = input_data.splitlines()
    columns = [''.join(x) for x in zip_longest(*lines, fillvalue=' ')]
    groups = [list(g) for k, g in groupby(
        columns, key=lambda x: x.strip() == '') if not k]
    problems = [Problem(
        numbers=list(map(parse_int, group)),
        operator=add if group[0][-1] == "+" else mul
    ) for group in groups]
    return problems


def parse_part1(input_data: str) -> list[Problem]:
    lines = input_data.strip().splitlines()
    nums = [list(map(int, line.split())) for line in lines[:-1]]
    operators = lines[-1].split()
    problems = [
        Problem(
            numbers=[nums[row][col]for row in range(len(nums))],
            operator=add if operators[col] == "+" else mul)
        for col in range(len(nums[0]))
    ]
    return problems


def solve(input_data: str) -> tuple[int, int]:
    part1_data = parse_part1(input_data)
    part2_data = parse_part2(input_data)
    return compute_problems(part1_data), compute_problems(part2_data)
