from .field_parser import MinuteFieldParser, HourFieldParser, DayOfMonthFieldParser, MonthFieldParser, DayOfWeekFieldParser
from .command_handler import CommandHandler


class CronExpression:
    def __init__(self, expression):
        fields = expression.split()
        self.minutes = MinuteFieldParser().parse(fields[0])
        self.hours = HourFieldParser().parse(fields[1])
        self.days_of_month = DayOfMonthFieldParser().parse(fields[2])
        self.months = MonthFieldParser().parse(fields[3])
        self.days_of_week = DayOfWeekFieldParser().parse(fields[4])
        self.command = CommandHandler(fields[5]).command

    def display(self):
        print("minute        ", " ".join(map(str, self.minutes)))
        print("hour          ", " ".join(map(str, self.hours)))
        print("day of month  ", " ".join(map(str, self.days_of_month)))
        print("month         ", " ".join(map(str, self.months)))
        print("day of week   ", " ".join(map(str, self.days_of_week)))
        print("command       ", self.command)

