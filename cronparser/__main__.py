import sys
from .cron_expression import CronExpression

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m cronparser <cron_expression>")
        sys.exit(1)
    
    cron_string = sys.argv[1]
    cron_expression = CronExpression(cron_string)
    cron_expression.display()

if __name__ == "__main__":
    main()