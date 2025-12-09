from dataclasses import dataclass
from functools import reduce
import math


@dataclass
class Vec3:
    x: int
    y: int
    z: int

    def __str__(self) -> str:
        return f"({self.x},{self.y},{self.z})"

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


@dataclass
class Line3:
    start: Vec3
    end: Vec3

    @property
    def distance(self) -> float:
        return math.sqrt(
            (self.end.x - self.start.x) ** 2
            + (self.end.y - self.start.y) ** 2
            + (self.end.z - self.start.z) ** 2
        )

    @property
    def inverse(self) -> "Line3":
        return Line3(start=self.end, end=self.start)

    def __hash__(self) -> int:
        return hash((self.start, self.end))


def part1(
    lines: list[Line3],
    num_connections: int = 1000,
) -> int:
    circuits: list[set[Vec3]] = []
    count = 0
    first_lines = lines[:num_connections]
    while first_lines:
        count += 1
        line = first_lines.pop(0)
        circuits = add_connection(circuits, line.start, line.end)

    sorted_circuit_sizes = sorted([len(c) for c in circuits], reverse=True)
    return reduce(lambda x, y: x * y, sorted_circuit_sizes[:3])


def part2(num_points: int, lines: list[Line3]) -> int:
    circuits: list[set[Vec3]] = []
    last_circuit_value = 0
    while not circuits or len(circuits[0]) < num_points:
        line = lines.pop(0)
        last_circuit_value = line.start.x * line.end.x
        circuits = add_connection(circuits, line.start, line.end)
    return last_circuit_value


def add_connection(circuits: list[set[Vec3]], p1: Vec3, p2: Vec3) -> list[set[Vec3]]:
    p1_idx = None
    p2_idx = None
    for i, circuit in enumerate(circuits):
        if p1 in circuit:
            p1_idx = i
        if p2 in circuit:
            p2_idx = i
        if p1_idx is not None and p2_idx is not None:
            break

    # Merge circuits if both points are found
    if p1_idx is not None and p2_idx is not None:
        # Ignore if both points are already in the same circuit
        if p1_idx != p2_idx:
            circuits[p1_idx] = circuits[p1_idx].union(circuits[p2_idx])
            del circuits[p2_idx]
    # Add point to existing circuit
    elif p1_idx is not None or p2_idx is not None:
        index: int = p1_idx if p1_idx is not None else p2_idx  # pyright: ignore[reportAssignmentType]
        circuit = circuits[index]
        circuit.add(p1)
        circuit.add(p2)
    # Create new circuit
    else:
        circuits.append({p1, p2})
    return circuits


def sorted_lines(
    points: list[Vec3],
) -> list[Line3]:
    lines = set[Line3]()
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i + 1 :]):
            if i == j:
                continue
            line = Line3(start=p1, end=p2)
            if line in lines or line.inverse in lines:
                continue
            lines.add(line)

    return sorted(lines, key=lambda line: line.distance)


def parse_input(input_data: str) -> list[Vec3]:
    nums = [map(int, line.split(",")) for line in input_data.strip().splitlines()]
    points = [Vec3(x=x, y=y, z=z) for x, y, z in nums]
    return points


def solve(input_data: str, num_connections: int = 1000) -> tuple[int, int]:
    points = parse_input(input_data)
    lines = sorted_lines(points)
    return part1(lines, num_connections), part2(len(points), lines)
