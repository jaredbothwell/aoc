from functools import reduce


def pick_from_bank(remaining: list[int], count: int) -> list[int]:
    end = len(remaining) - count + 1
    max_val = max(remaining[:end])
    max_index = remaining.index(max_val)
    if count == 1:
        return [max_val]
    return [max_val] + pick_from_bank(remaining[max_index + 1 :], count - 1)


def digits_to_int(digits: list[int]) -> int:
    return reduce(lambda acc, d: acc * 10 + d, digits, 0)


def maximize_joltage(banks: list[list[int]], count: int) -> int:
    total = 0
    for bank in banks:
        digits = pick_from_bank(bank, count)
        joltage = digits_to_int(digits)
        total += joltage
    return total


def parse_input(input_data: str) -> list[list[int]]:
    return [[int(c) for c in bank] for bank in input_data.splitlines()]


def solve(input_data: str) -> tuple[int, int]:
    banks = parse_input(input_data)
    part1 = maximize_joltage(banks, 2)
    part2 = maximize_joltage(banks, 12)
    return part1, part2
