from pathlib import Path

input_file_name = "input.txt"
solution_file_name = "solution.py"
test_file_name = "test_solution.py"
template_dir = Path(__file__).parent / "templates"

solution_template_file_path = template_dir / solution_file_name
test_template_file_path = template_dir / test_file_name


def format_day(day: int) -> str:
    return f"day{day:02d}"


def format_year(year: int) -> str:
    return str(year)


def get_day_path(year: int, day: int) -> Path:
    year_str = format_year(year)
    day_str = format_day(day)
    return Path(__file__).parent / "years" / year_str / day_str


def get_input_file_path(year: int, day: int) -> Path:
    return get_day_path(year, day) / input_file_name


def get_test_file_path(year: int, day: int) -> Path:
    return get_day_path(year, day) / test_file_name


def get_solution_file_path(year: int, day: int) -> Path:
    return get_day_path(year, day) / solution_file_name


def get_solution_module_name(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return f"aoc.years.{year_str}.{day_str}.solution"


def get_test_module_name(year: int, day: int) -> str:
    year_str = format_year(year)
    day_str = format_day(day)
    return f"aoc.years.{year_str}.{day_str}.test_solution"
