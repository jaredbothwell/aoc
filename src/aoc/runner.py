import argparse
from datetime import datetime
import importlib
import logging
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


from aoc.paths import (
    get_input_file_path,
    get_solution_module_name,
    get_test_input_dir_path,
)

logger = logging.getLogger(__name__)


def run_official_input(year: int, day: int) -> None:
    input_file = get_input_file_path(year, day)
    logger.info("")
    logger.info("-" * 80)
    logger.info(f"Running official input file: {input_file}")
    run_solution(year, day, input_file)


def run_test_input(year: int, day: int) -> None:
    test_dir = get_test_input_dir_path(year, day)
    test_files = list(test_dir.glob("*.txt"))
    test_files.sort()

    for test_file in test_files:
        logger.info("")
        logger.info("-" * 80)
        logger.info(f"Running test input file: {test_file}")
        run_solution(year, day, test_file)


def run_solution(year: int, day: int, input_file: Path) -> None:
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
            sys.exit(1)

        part1, part2 = solution_module.solve(input_data)

    except Exception as e:
        logger.error(f"Error while running solve() in {module_name}: {e}")
        sys.exit(1)

    logger.info(f"Part 1: {part1}")
    logger.info(f"Part 2: {part2}")
    logger.info("-" * 80)


def main() -> None:
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

    runner_function = run_test_input if args.test else run_official_input
    runner_function(year=args.year, day=args.day)


if __name__ == "__main__":
    main()
