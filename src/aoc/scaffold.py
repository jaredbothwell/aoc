import argparse
import logging
import os
from typing import Optional

import requests

from aoc.format import (
    format_input_file_path,
    format_solution_file_path,
    format_test_input_file_path,
)
from aoc.utils import coerce_dates

logger = logging.getLogger(__name__)


def scaffold_aoc_day(year: Optional[int] = None, day: Optional[int] = None) -> None:
    year, day = coerce_dates(year, day)

    # Create files if they do not exist
    create_input_file(year, day)
    create_test_input_file(year, day)
    create_solution_file(year, day)

    logger.info(f"Created scaffold for AoC {year} Day {day:02d}")


def fetch_input_data(year: int, day: int) -> str:
    try:
        session_token = os.getenv("AOC_SESSION_TOKEN")
        if not session_token:
            raise RuntimeError("AOC_SESSION_TOKEN environment variable not set.")
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        response = requests.get(url, cookies={"session": session_token})
        if not response.ok:
            raise RuntimeError(
                f"Failed to fetch input data from {url}: {response.status_code} {response.reason}"
            )

        logger.info(f"Successfully loaded input data for AoC {year} Day {day}")
        return response.text
    except Exception as e:
        logger.error(f"Error fetching input data: {e}")
        return ""


def create_input_file(year: int, day: int) -> None:
    input_file_path = format_input_file_path(year, day)
    os.makedirs(input_file_path.parent, exist_ok=True)
    if input_file_path.exists():
        logger.info(
            f"Input file already exists at {input_file_path}, skipping creation."
        )
        return
    logger.info(f"Creating input file at {input_file_path}")
    response_text = fetch_input_data(year, day)

    with open(input_file_path, "w") as input_file:
        input_file.write(response_text)
    logger.info(f"Created input file at {input_file_path}")


def create_test_input_file(year: int, day: int) -> None:
    test_input_file_path = format_test_input_file_path(year, day)
    os.makedirs(test_input_file_path.parent, exist_ok=True)
    if test_input_file_path.exists():
        logger.info(
            f"Test input file already exists at {test_input_file_path}, skipping creation."
        )
        return
    logger.info(f"Creating test input file at {test_input_file_path}")
    with open(test_input_file_path, "w") as test_input_file:
        test_input_file.writelines(
            [
                '"""',
                "Add your test input data here",
                "Can have multiple test input files named test_input01.txt, test_input02.txt, etc.",
                '"""',
            ]
        )


def create_solution_file(year: int, day: int) -> None:
    solution_file_path = format_solution_file_path(year, day)
    if solution_file_path.exists():
        logger.info(
            f"Solution file already exists at {solution_file_path}, skipping creation."
        )
        return
    logger.info(f"Creating solution file at {solution_file_path}")
    with open("src/aoc/template_solution.py", "r") as template_file:
        template_content = template_file.read()
    with open(solution_file_path, "w") as solution_file:
        solution_file.write(template_content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a new Advent of Code day directory structure."
    )
    parser.add_argument(
        "--year",
        type=int,
        help="The year of the Advent of Code (default: current year)",
    )
    parser.add_argument(
        "--day",
        type=int,
        help="The day of the Advent of Code (default: current day)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    scaffold_aoc_day(year=args.year, day=args.day)


if __name__ == "__main__":
    main()
