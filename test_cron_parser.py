import unittest
from cron_parser import parse_cron_expression, parse_cron_field, expand_range_with_step

class TestCronParser(unittest.TestCase):
    def test_simple_values(self):
        """Test parsing of fields with simple values."""
        self.assertEqual(parse_cron_field("5", 0, 59), [5])
        self.assertEqual(parse_cron_field("0", 0, 23), [0])

    def test_ranges(self):
        """Test parsing of fields with ranges."""
        self.assertEqual(parse_cron_field("1-3", 0, 59), [1, 2, 3])
        self.assertEqual(parse_cron_field("4-5", 1, 12), [4, 5])

    def test_steps(self):
        """Test parsing of fields with steps."""
        self.assertEqual(parse_cron_field("*/15", 0, 59), [0, 15, 30, 45])
        self.assertEqual(parse_cron_field("*/3", 0, 23), list(range(0, 24, 3)))

    def test_range_with_step(self):
        """Test parsing of fields with ranges and steps."""
        self.assertEqual(parse_cron_field("1-10/2", 0, 59), [1, 3, 5, 7, 9])
        self.assertEqual(parse_cron_field("10-20/3", 1, 31), [10, 13, 16, 19])

    def test_lists(self):
        """Test parsing of fields with lists of values."""
        self.assertEqual(parse_cron_field("1,3,5", 0, 59), [1, 3, 5])
        self.assertEqual(parse_cron_field("2,4,6", 0, 23), [2, 4, 6])

    def test_invalid_input(self):
        """Test handling of invalid input."""
        with self.assertRaises(ValueError):
            parse_cron_field("60", 0, 59)
        with self.assertRaises(ValueError):
            parse_cron_field("-1", 0, 23)

    def test_full_expression(self):
        """Test parsing of a full cron expression."""
        result = parse_cron_expression("*/15 0 1,15 * 1-5 /usr/bin/find")
        self.assertEqual(result, {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day of month": [1, 15],
            "month": list(range(1, 13)),
            "day of week": [1, 2, 3, 4, 5],
            "command": "/usr/bin/find"
        })

if __name__ == "__main__":
    unittest.main()
