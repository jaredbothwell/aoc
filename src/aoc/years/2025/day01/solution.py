def part1(input_data: str) -> int:
    count = 0
    dial = 50
    lines = input_data.strip().splitlines()
    for line in lines:
        direction, distance = line[0], int(line[1:].strip())
        if direction == "L":
            dial -= distance
            dial %= 100
        elif direction == "R":
            dial += distance
            dial %= 100
        if dial == 0:
            count += 1
    return count


def part2(input_data: str) -> int:
    count = 0
    dial = 50
    lines = input_data.strip().splitlines()
    for line in lines:
        direction, distance = line[0], int(line[1:].strip())
        while distance > 0:
            distance -= 1
            dial += 1 if direction == "R" else -1
            dial %= 100
            if dial == 0:
                count += 1
    return count


def solve(input_data: str) -> tuple[int, int]:
    return part1(input_data), part2(input_data)
