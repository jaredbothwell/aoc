from aoc.utils.interval import ClosedInterval


def part1(merged_intervals: list[ClosedInterval], values: list[int]) -> int:
    max_value = max(interval.end for interval in merged_intervals)
    count = 0
    for value in values:
        if value > max_value:
            break
        for interval in merged_intervals:
            if interval.contains(value):
                count += 1
                break
            if value < interval.start:
                break
    return count


def part2(merged_intervals: list[ClosedInterval]) -> int:
    return sum(interval.size for interval in merged_intervals)


def merge_intervals(intervals: list[ClosedInterval]) -> list[ClosedInterval]:
    merged_intervals = [intervals[0]]
    for i in intervals[1:]:
        curr = merged_intervals[-1]
        if curr.can_merge_with(i):
            curr.end = max(curr.end, i.end)
        else:
            merged_intervals.append(i)
    return merged_intervals


def parse_input(input_data: str) -> tuple[list[ClosedInterval], list[int]]:
    top, bottom = input_data.split("\n\n")
    intervals = sorted(
        [ClosedInterval(*map(int, line.split("-"))) for line in top.splitlines()],
        key=lambda x: x.start,
    )
    values = sorted(map(int, bottom.splitlines()))
    merged_intervals = merge_intervals(intervals)
    return merged_intervals, values


def solve(input_data: str) -> tuple[int, int]:
    merged_intervals, values = parse_input(input_data)
    return part1(merged_intervals, values), part2(merged_intervals)
