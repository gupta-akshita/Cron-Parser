import sys

def expand_range_with_step(value, range_min, range_max):
    """
    Expand cron field values that include a step, handling both entire and partial ranges.
    
    Args:
        value (str): The field value, potentially including a range and/or step.
        range_min (int): The minimum acceptable value for this field.
        range_max (int): The maximum acceptable value for this field.
    
    Returns:
        list: Expanded list of integers representing the specified times.
    
    Raises:
        ValueError: If the range or step is invalid.
    """
    try:
        parts = value.split("/")
        step = int(parts[1]) if len(parts) > 1 else 1
        if "-" in parts[0]:
            start, end = map(int, parts[0].split("-"))
            if start > end:
                raise ValueError("Range start must not exceed range end.")
        elif parts[0] == "*":
            start, end = range_min, range_max
        else:
            raise ValueError("Invalid range or step syntax.")
        return list(range(start, end + 1, step))
    except ValueError as e:
        raise ValueError(f"Invalid step or range in field value '{value}': {e}")

def parse_cron_field(field, range_min, range_max):
    """
    Parse a single cron field, expanding it into all times it specifies within the allowed range.
    
    Handles individual numbers, ranges (e.g., 1-3), lists (e.g., 1,2,3), steps (e.g., */2),
    and combinations thereof.
    
    Args:
        field (str): The cron field to parse.
        range_min (int): Minimum allowable value for this field.
        range_max (int): Maximum allowable value for this field.
    
    Returns:
        list: A list of integers representing the parsed field values.
    
    Raises:
        ValueError: If the field contains invalid characters or formats.
    """
    # Directly return all possible values for wildcard without step
    if field == "*":
        return list(range(range_min, range_max + 1))
    
    # Split field into parts if it contains commas, indicating a list of values or ranges
    parts = field.split(",")
    results = []
    for part in parts:
        if "/" in part or "-" in part:
            # Expand ranges and steps into individual values
            results.extend(expand_range_with_step(part, range_min, range_max))
        else:
            # Handle individual numbers, verifying their validity
            if not part.isdigit() or not range_min <= int(part) <= range_max:
                raise ValueError(f"Invalid field value: '{part}'")
            results.append(int(part))
    # Ensure no duplicate times and preserve chronological order
    return sorted(set(results))

def parse_cron_expression(expr):
    """
    Parse a full cron expression, including its command, into a dictionary mapping each time field
    to its list of specified times, and including the command itself.
    
    Args:
        expr (str): The cron expression to parse.
    
    Returns:
        dict: A dictionary with keys for 'minute', 'hour', 'day of month', 'month', 'day of week', and 'command'.
    
    Raises:
        ValueError: For invalid cron expressions.
    """
    parts = expr.split()
    if len(parts) != 6:
        raise ValueError("Invalid cron expression format. Expected 5 time fields plus a command.")
    minute, hour, dom, month, dow, command = parts
    return {
        "minute": parse_cron_field(minute, 0, 59),
        "hour": parse_cron_field(hour, 0, 23),
        "day of month": parse_cron_field(dom, 1, 31),
        "month": parse_cron_field(month, 1, 12),
        "day of week": parse_cron_field(dow, 0, 6),
        "command": command
    }

def main(cron_expr):
    """
    Main function. Parses a given cron expression and prints the schedule in a human-readable format.
    
    Args:
        cron_expr (str): The cron expression to parse.
    """
    try:
        results = parse_cron_expression(cron_expr)
        for field, times in results.items():
            print(f"{field:14} {' '.join(map(str, times)) if field != 'command' else times}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cron_parser.py '<cron_string>'")
        sys.exit(1)
    main(sys.argv[1])
