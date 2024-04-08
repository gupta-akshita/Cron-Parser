import re

class FieldParser:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def parse(self, field_str):
        if field_str == '*':
            return list(range(self.min_val, self.max_val + 1))
        elif '-' in field_str:
            start, end = map(int, field_str.split('-'))
            return list(range(start, end + 1))
        elif ',' in field_str:
            return list(map(int, field_str.split(',')))
        elif '/' in field_str:
            step = int(field_str.split('/')[1])
            return list(range(self.min_val, self.max_val + 1, step))
        else:  # single value
            return [int(field_str)]

class MinuteFieldParser(FieldParser):
    def __init__(self):
        super().__init__(0, 59)

class HourFieldParser(FieldParser):
    def __init__(self):
        super().__init__(0, 23)

class DayOfMonthFieldParser(FieldParser):
    def __init__(self):
        super().__init__(1, 31)

class MonthFieldParser(FieldParser):
    def __init__(self):
        super().__init__(1, 12)

class DayOfWeekFieldParser(FieldParser):
    def __init__(self):
        super().__init__(0, 6)  # Typically 0 = Sunday, 6 = Saturday
