def neighbor_positions(x: int, y: int) -> list[tuple[int, int]]:
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]


def bounded_neighbors(x: int, y: int, grid: list[list[str]]) -> list[str]:
    neighbors: list[str] = []
    for nx, ny in neighbor_positions(x, y):
        if 0 <= nx and nx < len(grid[0]) and 0 <= ny and ny < len(grid):
            neighbors.append(grid[ny][nx])
    return neighbors


def find_removable_positions(grid: list[list[str]]) -> list[tuple[int, int]]:
    removable_positions: list[tuple[int, int]] = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != "@":
                continue

            neighbors = bounded_neighbors(x, y, grid)
            neighbor_count = len([n for n in neighbors if n == "@"])
            if neighbor_count < 4:
                removable_positions.append((x, y))
    return removable_positions


def part1(grid: list[list[str]]) -> int:
    return len(find_removable_positions(grid))


def part2(grid: list[list[str]]) -> int:
    total_removed = 0
    last_removed = None

    while last_removed != 0:
        removable_positions = find_removable_positions(grid)
        for x, y in removable_positions:
            grid[y][x] = "."
        last_removed = len(removable_positions)
        total_removed += last_removed

    return total_removed


def solve(input_data: str) -> tuple[int, int]:
    grid = [list(x) for x in input_data.splitlines()]
    return part1(grid), part2(grid)
