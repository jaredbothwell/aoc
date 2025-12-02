import os
from datetime import datetime
from pathlib import Path
from typing import Optional
import argparse
import logging
import requests

logger = logging.getLogger(__name__)

def scaffold_aoc_day(year: Optional[int] = None, day: Optional[int] = None) -> None:
    if year is None or day is None:
        now = datetime.now()
        if year is None: year = now.year
        if day is None: day = now.day

    day_str = f"day{day:02d}"
    base_path = Path(f"src/aoc/{year}/{day_str}")
    os.makedirs(base_path, exist_ok=True)

    input_file_path = base_path / "input.txt"
    if not bool(input_file_path.exists()):
        create_input_file(input_file_path, year, day)

    test_input_file_path = base_path / "tests/test_input01.txt"
    if not bool(test_input_file_path.exists()):
        create_test_input_file(test_input_file_path)

    solution_file_path = base_path / "solution.py"
    if not bool(solution_file_path.exists()):
        create_solution_file(solution_file_path)
            
    logger.info(f"Created scaffold for AoC {year} Day {day:02d} at {base_path}")

def create_input_file(path: Path, year: int, day: int) -> None:
    logger.info(f"Creating input file at {path}")
    session_token = os.getenv("AOC_SESSION")
    if not session_token:
        logger.error("AOC_SESSION environment variable not set. Cannot fetch input data.")
        return
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(url, cookies={"session": session_token})
    if response.status_code == 200:
        with open(path, "w") as input_file:
            input_file.write(response.text)
        logger.info(f"Fetched and created input file at {path}")
    else:
        logger.error(f"Failed to fetch input data from {url}")

def create_test_input_file(path: Path) -> None:
    logger.info(f"Creating test input file at {path}")
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w") as test_input_file:
        test_input_file.write("# Add your test input data here\n# Can have multiple test input files named test_input01.txt, test_input02.txt, etc.\n")


def create_solution_file(path: Path) -> None:
    logger.info(f"Creating solution file at {path}")
    with open("src/aoc/template_solution.py", "r") as template_file:
        template_content = template_file.read()
        with open(path, "w") as solution_file:
            solution_file.write(template_content)

def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new Advent of Code day directory structure."
    )
    parser.add_argument(
        "year", type=int, help="The year of the Advent of Code (default: current year)"
    )
    parser.add_argument(
        "day", type=int, help="The day of the Advent of Code (default: current day)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    scaffold_aoc_day(year=args.year, day=args.day)

if __name__ == "__main__":
    main()