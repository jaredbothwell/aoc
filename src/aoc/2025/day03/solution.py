def pick_from_bank(remaining_in_bank: list[int], count: int) -> list[int]:
    max_val = -1
    max_index = -1
    end = len(remaining_in_bank) - count + 1
    for i, val in enumerate(remaining_in_bank[:end]):
        if val > max_val:
            max_val = val
            max_index = i

    if count == 1:
        return [max_val]
    return [max_val] + pick_from_bank(remaining_in_bank[max_index + 1 :], count - 1)


def maximize_joltage(banks: list[list[int]], picks: int) -> int:
    return sum(
        [int("".join(str(x) for x in pick_from_bank(bank, picks))) for bank in banks]
    )


def solve(input_data: str) -> tuple[int, int]:
    banks = [[int(c) for c in bank] for bank in input_data.splitlines()]
    part1 = maximize_joltage(banks, 2)
    part2 = maximize_joltage(banks, 12)
    return part1, part2
