from collections import defaultdict


def split_beams(rows: list[str]) -> tuple[int, int]:
    start_col = rows[0].index("S")
    current_beams = {start_col: 1}
    split_count = 0
    for row in rows[1:]:
        next_beams = defaultdict[int, int](int)
        for col, beam_count in current_beams.items():
            if row[col] == "^":
                split_count += 1
                next_beams[col - 1] += beam_count
                next_beams[col + 1] += beam_count
            else:
                next_beams[col] += beam_count
        current_beams = next_beams
    return split_count, sum(current_beams.values())


def solve(input_data: str) -> tuple[int, int]:
    return split_beams(input_data.splitlines())
