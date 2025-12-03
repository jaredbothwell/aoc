from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


def coerce_dates(year: Optional[int], day: Optional[int]) -> tuple[int, int]:
    """Coerce year and day to valid integers based on current date if None.
    Year and day default to current year and day in Eastern Time since AoC
    resets at midnight EST.

    Args:
        year (Optional[int]): The year to coerce.
        day (Optional[int]): The day to coerce.

    Returns:
        tuple[int, int]: A tuple containing the coerced year and day.
    """

    now = datetime.now(ZoneInfo("America/New_York"))
    coerced_year = year if year is not None else now.year
    coerced_day = day if day is not None else now.day
    return coerced_year, coerced_day
