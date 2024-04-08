import pytest
from cronparser.cron_expression import CronExpression

@pytest.mark.parametrize("cron_string, expected_minutes, expected_hours, expected_days_of_month, expected_months, expected_days_of_week, expected_command", [
    ("*/15 0 1,15 * 1-5 /usr/bin/find", [0, 15, 30, 45], [0], [1, 15], list(range(1, 13)), [1, 2, 3, 4, 5], "/usr/bin/find"),
    ("0 * * * * /usr/bin/command", [0], list(range(0, 24)), list(range(1, 32)), list(range(1, 13)), list(range(0, 7)), "/usr/bin/command"),
    ("0 0 * * * /usr/bin/nightly-job", [0], [0], list(range(1, 32)), list(range(1, 13)), list(range(0, 7)), "/usr/bin/nightly-job"),
    ("30 8 * * 1-5 /usr/bin/weekday-job", [30], [8], list(range(1, 32)), list(range(1, 13)), [1, 2, 3, 4, 5], "/usr/bin/weekday-job"),
    ("0 0 1 * * /usr/bin/monthly-job", [0], [0], [1], list(range(1, 13)), list(range(0, 7)), "/usr/bin/monthly-job"),
    ("0 0 * * 0 /usr/bin/sunday-job", [0], [0], list(range(1, 32)), list(range(1, 13)), [0], "/usr/bin/sunday-job"),
    ])

def test_cron_expression(cron_string, expected_minutes, expected_hours, expected_days_of_month, expected_months, expected_days_of_week, expected_command):
    cron_expression = CronExpression(cron_string)
    assert cron_expression.minutes == expected_minutes
    assert cron_expression.hours == expected_hours
    assert cron_expression.days_of_month == expected_days_of_month
    assert cron_expression.months == expected_months
    assert cron_expression.days_of_week == expected_days_of_week
    assert cron_expression.command == expected_command
