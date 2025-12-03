from pathlib import Path

input_file_name = "input.txt"
test_input_file_name = "test_input_01.txt"
tests_folder_name = "tests"
solution_file_name = "solution.py"


def format_day(day: int) -> str:
    return f"day{day:02d}"


def format_year(year: int) -> str:
    return str(year)


def format_input_file_path(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return Path(__file__).parent / year_str / day_str / input_file_name


def format_test_input_file_path(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return (
        Path(__file__).parent
        / year_str
        / day_str
        / tests_folder_name
        / test_input_file_name
    )


def format_solution_file_path(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return Path(__file__).parent / year_str / day_str / solution_file_name


def format_solution_module_name(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return f"aoc.{year_str}.{day_str}.solution"
