from dataclasses import dataclass


@dataclass
class ClosedInterval:
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError(
                f"Invalid interval with start greater than end: start={self.start}, end={self.end}"
            )

    @property
    def size(self) -> int:
        return self.end - self.start + 1

    def contains(self, value: int) -> bool:
        return self.start <= value <= self.end

    def can_merge_with(self, other: "ClosedInterval") -> bool:
        return self.start <= other.end + 1 and other.start <= self.end + 1


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
