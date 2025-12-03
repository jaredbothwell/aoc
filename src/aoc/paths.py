from pathlib import Path

input_file_name = "input.txt"
default_test_input_file_name = "test_input_01.txt"
tests_folder_name = "tests"
solution_file_name = "solution.py"


def format_day(day: int) -> str:
    return f"day{day:02d}"


def format_year(year: int) -> str:
    return str(year)


def get_input_file_path(year: int, day: int) -> Path:
    year_str = format_year(year)
    day_str = format_day(day)
    return Path(__file__).parent / year_str / day_str / input_file_name


def get_test_input_dir_path(year: int, day: int) -> Path:
    year_str = format_year(year)
    day_str = format_day(day)
    return Path(__file__).parent / year_str / day_str / tests_folder_name


def get_default_test_input_file_path(year: int, day: int) -> Path:
    return get_test_input_dir_path(year, day) / default_test_input_file_name


def get_solution_file_path(year: int, day: int) -> Path:
    year_str = format_year(year)
    day_str = format_day(day)
    return Path(__file__).parent / year_str / day_str / solution_file_name


def get_solution_module_name(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return f"aoc.{year_str}.{day_str}.solution"
