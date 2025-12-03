import argparse
import importlib
import logging
import sys
from typing import Optional


from aoc.format import (
    format_input_file_path,
    format_solution_module_name,
)
from aoc.utils import coerce_dates

logger = logging.getLogger(__name__)


def run_solution(year: Optional[int], day: Optional[int]) -> None:
    year, day = coerce_dates(year, day)
    module_name = format_solution_module_name(year, day)
    input_file = format_input_file_path(year, day)
    logger.info(f"Running AoC {year} Day {day:02d} solution from {module_name}")
    if not input_file.exists():
        logger.error(f"Input file not found: {input_file}")
        sys.exit(1)

    try:
        solution_module = importlib.import_module(module_name)
    except ImportError as e:
        logger.error(f"Could not import module {module_name}: {e}")
        sys.exit(1)

    if not hasattr(solution_module, "solve"):
        logger.error(f"No solve() function found in {module_name}")
        sys.exit(1)

    try:
        with open(input_file, "r") as f:
            input_data = f.read()
        part1, part2 = solution_module.solve(input_data)
    except Exception as e:
        logger.error(f"Error while running solve() in {module_name}: {e}")
        sys.exit(1)

    logger.info("------------------------------------------")
    logger.info(f"Year {year} Day {day:02d} Solutions:")
    logger.info(f"Part 1: {part1}")
    logger.info(f"Part 2: {part2}")
    logger.info("------------------------------------------")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solution for a specific year and day."
    )
    parser.add_argument("--year", type=int, help="Year of the Advent of Code")
    parser.add_argument("--day", type=int, help="Day of the Advent of Code")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    run_solution(year=args.year, day=args.day)


if __name__ == "__main__":
    main()
