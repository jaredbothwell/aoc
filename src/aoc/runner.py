
import argparse
from datetime import datetime
import importlib
import logging
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

logger = logging.getLogger(__name__)


def get_solution_module(year: int, day: int) -> tuple[str, Path]:
    day_str = f"day{day:02d}"
    year_str = f"{year}"
    module_name = f"aoc.{year_str}.{day_str}.solution"
    input_dir = Path(__file__).parent / year_str / day_str
    return module_name, input_dir

def main():
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solution for a specific year and day."
    )
    parser.add_argument("--year", type=int, help="Year of the Advent of Code")
    parser.add_argument("--day", type=int, help="Day of the Advent of Code")
    args = parser.parse_args()
    year = args.year
    day = args.day
    if year is None or day is None:
        now = datetime.now(ZoneInfo("America/New_York")) # AoC uses Eastern Time
        if year is None: year = now.year
        if day is None: day = now.day

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    module_name, input_dir = get_solution_module(year, day)
    input_file = input_dir / "input.txt"
    logger.info(f"Running AoC {year} Day {day:02d} solution from {module_name} with input file {input_file}")
    if not input_file.exists():
        logger.error(f"Input file not found: {input_file}")
        return
 
    try:
        solution_module = importlib.import_module(module_name)
    except ImportError as e:
        logger.error(f"Could not import module {module_name}: {e}")
        return

    if not hasattr(solution_module, "solve"):
        logger.error(f"No solve() function found in {module_name}")
        return
    
    try:
        with open(input_file, "r") as f:
            input_data = f.read()
        part1, part2 = solution_module.solve(input_data)
    except Exception as e:
        logger.error(f"Error while running solve() in {module_name}: {e}")
        return

    logger.info(f"\n---------------\nYear {year} Day {day:02d} Solutions:")
    logger.info(f"Part 1: {part1}")
    logger.info(f"Part 2: {part2}")

if __name__ == "__main__":
    main()