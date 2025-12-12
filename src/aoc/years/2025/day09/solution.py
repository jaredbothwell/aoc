def part1(coordinates_list: list[tuple[int, int]]) -> int:
    max_rect_area = 0
    for i, c1 in enumerate(coordinates_list):
        for c2 in coordinates_list[i + 1 :]:
            x1, y1 = c1
            x2, y2 = c2
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_rect_area:
                max_rect_area = area

    return max_rect_area


def part2(coordinates_list: list[tuple[int, int]]) -> int:
    x_vals = sorted(x for x, _ in coordinates_list)
    y_vals = sorted(y for _, y in coordinates_list)
    x_map = {x: i for i, x in enumerate(x_vals)}
    y_map = {y: i for i, y in enumerate(y_vals)}

    grid = [["." for _ in range(len(y_vals) + 1)] for _ in range(len(x_vals) + 1)]

    for x, y in coordinates_list:
        mapped_x = x_map[x]
        mapped_y = y_map[y]
        grid[mapped_x][mapped_y] = "#"

    # Draw lines connecting the points
    prev = coordinates_list[-1]
    for curr in coordinates_list:
        x1, y1 = prev
        x2, y2 = curr
        mapped_x1 = x_map[x1]
        mapped_y1 = y_map[y1]
        mapped_x2 = x_map[x2]
        mapped_y2 = y_map[y2]

        if mapped_x1 == mapped_x2:
            for y in range(min(mapped_y1, mapped_y2), max(mapped_y1, mapped_y2) + 1):
                grid[mapped_x1][y] = "#"
        elif mapped_y1 == mapped_y2:
            for x in range(min(mapped_x1, mapped_x2), max(mapped_x1, mapped_x2) + 1):
                grid[x][mapped_y1] = "#"

        prev = curr

    ## Fill outside the shape with spaces by scanning from all four sides
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                break
            grid[r][c] = " "
        for c in range(cols - 1, -1, -1):
            if grid[r][c] == "#":
                break
            grid[r][c] = " "
    for c in range(cols):
        for r in range(rows):
            if grid[r][c] == "#":
                break
            grid[r][c] = " "
        for r in range(rows - 1, -1, -1):
            if grid[r][c] == "#":
                break
            grid[r][c] = " "

    # Find max rectangle between the "#" characters without covering any spaces
    max_rect_area = 0
    for i, c1 in enumerate(coordinates_list):
        for _, c2 in enumerate(coordinates_list[i + 1 :]):
            x1, y1 = c1
            x2, y2 = c2

            # Grid coordinates are compressed
            compressed_x1, compressed_y1 = x_map[x1], y_map[y1]
            compressed_x2, compressed_y2 = x_map[x2], y_map[y2]

            min_x = min(compressed_x1, compressed_x2)
            max_x = max(compressed_x1, compressed_x2)
            min_y = min(compressed_y1, compressed_y2)
            max_y = max(compressed_y1, compressed_y2)

            valid_rectangle = True
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if grid[x][y] == " ":
                        valid_rectangle = False
                        break
                if not valid_rectangle:
                    break

            if valid_rectangle:
                width = x_vals[max_x] - x_vals[min_x] + 1
                height = y_vals[max_y] - y_vals[min_y] + 1
                area = width * height
                if area > max_rect_area:
                    max_rect_area = area

    return max_rect_area


def parse_input(input_data: str) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    for line in input_data.strip().splitlines():
        x_str, y_str = line.split(",")
        points.append((int(x_str), int(y_str)))
    return points


def solve(input_data: str) -> tuple[int, int]:
    parsed_data = parse_input(input_data)
    return part1(parsed_data), part2(parsed_data)
