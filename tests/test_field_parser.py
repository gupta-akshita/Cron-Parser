import pytest
from cronparser.field_parser import MinuteFieldParser, HourFieldParser, DayOfMonthFieldParser, MonthFieldParser, DayOfWeekFieldParser

# Testing MinuteFieldParser with various cases
@pytest.mark.parametrize("input,expected", [
    ("*", list(range(0, 60))),  # Every minute
    ("*/15", [0, 15, 30, 45]),  # Every 15 minutes
    ("1-5", [1, 2, 3, 4, 5]),    # Range: Minutes 1 through 5
    ("5", [5]),                  # Specific minute
    ("0,20,40", [0, 20, 40]),    # List of specific minutes
])
def test_minute_field_parser(input, expected):
    parser = MinuteFieldParser()
    assert parser.parse(input) == expected

# Example structure for other parsers
@pytest.mark.parametrize("input,expected", [
    # Include tests for every hour, specific hours, ranges, steps, and lists
])
def test_hour_field_parser(input, expected):
    parser = HourFieldParser()
    assert parser.parse(input) == expected

@pytest.mark.parametrize("input,expected", [
    # Tests for day of month: every day, specific days, ranges, steps, and lists
])
def test_day_of_month_field_parser(input, expected):
    parser = DayOfMonthFieldParser()
    assert parser.parse(input) == expected

@pytest.mark.parametrize("input,expected", [
    # Tests for month: every month, specific months, ranges, steps, and lists
])
def test_month_field_parser(input, expected):
    parser = MonthFieldParser()
    assert parser.parse(input) == expected

@pytest.mark.parametrize("input,expected", [
    # Tests for day of week: every day, specific days, ranges, steps, and lists
])
def test_day_of_week_field_parser(input, expected):
    parser = DayOfWeekFieldParser()
    assert parser.parse(input) == expected
