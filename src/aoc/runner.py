import argparse
import importlib
import logging
import sys
from datetime import datetime
from pathlib import Path
import traceback
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

from aoc.paths import (
    get_input_file_path,
    get_solution_module_name,
    get_test_module_name,
)

logger = logging.getLogger(__name__)


def run_tests(year: int, day: int) -> None:
    test_module_name = get_test_module_name(year, day)

    try:
        module = importlib.import_module(test_module_name)
    except ImportError as e:
        logger.error(f"Could not import module {test_module_name}: {e}")
        sys.exit(1)

    if not hasattr(module, "test_solution"):
        logger.error(f"No test_solution found in {test_module_name}")
        sys.exit(1)

    try:
        module.test_solution()
    except AssertionError as e:
        logger.error(f"Failed test: {e}")
    except Exception as e:
        logger.error(f"Error while running test_solution() in {test_module_name}: {e}")
        return


def run_solution(year: int, day: int) -> None:
    input_file = get_input_file_path(year, day)
    display_path = Path(*input_file.parts[5:])

    logger.info("")
    logger.info("-" * 80)
    logger.info(
        f"Running solution for year {year} day {day} using official input file: {display_path}"
    )
    module_name = get_solution_module_name(year, day)

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
            input_data = f.read().strip()
        if len(input_data) == 0:
            logger.error(f"Input file {input_file} is empty.")
            return

        part1, part2 = solution_module.solve(input_data)

    except Exception as e:
        logger.error(f"Error while running solve() in {module_name}: {e}")
        traceback.print_exc()

        return

    logger.info(f"Part 1: {part1}")
    logger.info(f"Part 2: {part2}")
    logger.info("-" * 80)


def main() -> None:
    load_dotenv()
    now = datetime.now(ZoneInfo("America/New_York"))

    parser = argparse.ArgumentParser(
        description="Run Advent of Code solution for a specific year and day."
    )
    parser.add_argument(
        "-y", "--year", type=int, default=now.year, help="Year of the Advent of Code"
    )
    parser.add_argument(
        "-d", "--day", type=int, default=now.day, help="Day of the Advent of Code"
    )

    parser.add_argument(
        "-t",
        "--test",
        default=False,
        action="store_true",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    runner_function = run_tests if args.test else run_solution
    runner_function(year=args.year, day=args.day)


if __name__ == "__main__":
    main()
