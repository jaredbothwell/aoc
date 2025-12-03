from typing import Callable


def part1_validation(num: int) -> bool:
    num_str = str(num)
    num_len = len(num_str)
    if num_len % 2 != 0:
        return False

    first_half = num_str[: num_len // 2]
    second_half = num_str[num_len // 2 :]

    return first_half == second_half


def part2_validation(num: int) -> bool:
    num_str = str(num)
    num_len = len(num_str)
    if num_len < 2:
        return False

    for size in range(num_len // 2, 0, -1):
        if num_len % size != 0:
            continue
        segments = [num_str[i : i + size] for i in range(0, num_len, size)]
        if all(segment == segments[0] for segment in segments):
            return True
    return False


def sum_invalid_numbers(input_data: str, check_function: Callable[[int], bool]) -> int:
    ranges = [x.split("-") for x in input_data.split(",")]
    invalid_nums = set()
    for start, end in ranges:
        for num in range(int(start), int(end) + 1):
            if num in invalid_nums:
                continue
            if check_function(num):
                invalid_nums.add(num)

    return sum(invalid_nums)


def solve(input_data: str) -> tuple[int, int]:
    part1 = sum_invalid_numbers(input_data, part1_validation)
    part2 = sum_invalid_numbers(input_data, part2_validation)
    return part1, part2
