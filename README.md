# Cron Parser

## Project Overview

The `cron_parser` project is a **command-line application** written in Python, designed to parse cron strings and expand each field to show the times at which a cron job will run. This tool supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command. It's crafted to be simple yet effective, omitting special time strings like "@yearly".

## Features

- **Parses standard cron strings** into a readable format.
- Supports all basic cron features, including **intervals** (`*/`), **ranges** (`-`), and **lists** (`,`).
- **Error handling** for unsupported or incorrectly formatted cron strings.

## Requirements

- **Python 3.6** or higher.

## Setup and Installation

No additional installation is required beyond having Python installed on your system. The parser is a standalone Python script, making it extremely accessible.

## Usage

To use the `cron_parser`, navigate to the directory containing the script and run it with a single argument: the cron string to be parsed. Here's the format:

```sh
python cron_parser.py "<cron_string>"
```

### Examples

Here’s a quick example to try:

```sh
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

**Expected Output:**

```
minute         0 15 30 45
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find
```

### Error Handling

Invalid cron strings will prompt an error message explaining the issue. Ensure your input adheres to the cron format for accurate parsing.

## Running Tests

Execute the included test suite with the following command, ensuring you're in the project directory:

```sh
python -m unittest test_cron_parser.py
```

This verifies the script's functionality and robustness across various scenarios.

## Contributing

Your contributions are welcome! Feel free to **fork the repository**, propose changes through pull requests, or submit issues for bugs and feature suggestions.

## License

This project is open-sourced under the **MIT License**. See the LICENSE file for more details.
