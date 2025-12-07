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

    def __len__(self) -> int:
        return self.end - self.start + 1

    def contains(self, value: int) -> bool:
        return self.start <= value <= self.end

    def can_merge_with(self, other: "ClosedInterval") -> bool:
        return self.start <= other.end + 1 and other.start <= self.end + 1
