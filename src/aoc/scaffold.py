import os
from datetime import datetime
from pathlib import Path
from typing import Optional
import argparse
import logging
from zoneinfo import ZoneInfo
import requests

logger = logging.getLogger(__name__)

def scaffold_aoc_day(year: Optional[int] = None, day: Optional[int] = None) -> None:
    if year is None or day is None:
        now = datetime.now(ZoneInfo("America/New_York")) # AoC uses Eastern Time
        if year is None: year = now.year
        if day is None: day = now.day

    day_str = f"day{day:02d}"
    base_path = Path(f"src/aoc/{year}/{day_str}")
    os.makedirs(base_path, exist_ok=True)

    # Create files if they do not exist
    create_input_file(base_path, year, day)
    create_test_input_file(base_path)
    create_solution_file(base_path)
            
    logger.info(f"Created scaffold for AoC {year} Day {day:02d} at {base_path}")

def create_input_file(base_path: Path, year: int, day: int) -> None:
    input_file_path = base_path / "input.txt"
    if input_file_path.exists():
        logger.info(f"Input file already exists at {input_file_path}, skipping creation.")
        return
    logger.info(f"Creating input file at {input_file_path}")
    session_token = os.getenv("AOC_SESSION")
    if not session_token:
        logger.error("AOC_SESSION environment variable not set. Cannot fetch input data.")
        return
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(url, cookies={"session": session_token})
    if not response.ok:
        logger.error(f"Failed to fetch input data from {url}: {response.status_code} {response.reason}")
        return
    
    with open(input_file_path, "w") as input_file:
        input_file.write(response.text)
    logger.info(f"Fetched and created input file at {input_file_path}")

def create_test_input_file(base_path: Path) -> None:
    test_input_file_path = base_path / "tests/test_input01.txt"
    if test_input_file_path.exists():
        logger.info(f"Test input file already exists at {test_input_file_path}, skipping creation.")
        return
    logger.info(f"Creating test input file at {test_input_file_path}")
    os.makedirs(test_input_file_path.parent, exist_ok=True)
    with open(test_input_file_path, "w") as test_input_file:
        test_input_file.write("# Add your test input data here\n# Can have multiple test input files named test_input01.txt, test_input02.txt, etc.\n")


def create_solution_file(base_path: Path) -> None:
    solution_file_path = base_path / "solution.py"
    if solution_file_path.exists():
        logger.info(f"Solution file already exists at {solution_file_path}, skipping creation.")
        return
    logger.info(f"Creating solution file at {solution_file_path}")
    with open("src/aoc/template_solution.py", "r") as template_file:
        template_content = template_file.read()
        with open(solution_file_path, "w") as solution_file:
            solution_file.write(template_content)

def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new Advent of Code day directory structure."
    )
    parser.add_argument(
        "--year", type=int, help="The year of the Advent of Code (default: current year)"
    )
    parser.add_argument(
        "--day", type=int, help="The day of the Advent of Code (default: current day)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    scaffold_aoc_day(year=args.year, day=args.day)

if __name__ == "__main__":
    main()