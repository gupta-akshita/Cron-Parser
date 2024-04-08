from cronparser import CronExpression

# Example cron string
cron_string = "*/15 0 1,15 * 1-5 /usr/bin/find"

cron_expression = CronExpression(cron_string)
cron_expression.display()
