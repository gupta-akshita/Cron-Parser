# Cron-Parser

Project Overview
  The cron_parser project is a command-line application written in Python. It's designed to parse cron strings, expanding each field to show the times at which a cron job will run. This tool supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command. It does not handle special time strings like "@yearly".
  
  The parser provides a straightforward and human-readable way to understand complex cron schedules, making it easier to grasp when certain cron jobs are supposed to execute.

Features
  Parses standard cron strings into a readable format.
  Supports all basic cron features, including intervals (*/), ranges (-), and lists (,).
  Error handling for unsupported or incorrectly formatted cron strings.
  Requirements
  Python 3.6 or higher.
  Setup and Installation
  No additional installation is required beyond having Python installed on your system. The parser is a standalone Python script.

Usage
  To use the cron_parser, navigate to the directory containing the script and run it with a single argument: the cron string to be parsed. The format for running the script is:
  
  sh
  Copy code
  python cron_parser.py "<cron_string>" or python3 cron_parser.py "<cron_string>"
  Examples
  Run the following command for a basic example:

  sh
  Copy code
  python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find" or python3 cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
  Output:

sql
  Copy code
  minute         0 15 30 45
  hour           0
  day of month   1 15
  month          1 2 3 4 5 6 7 8 9 10 11 12
  day of week    1 2 3 4 5
  command        /usr/bin/find
  Error Handling
  If an invalid cron string is provided, the script will display an error message detailing the issue. Make sure to input a valid cron format to get the expected results.

Running Tests
To run the test suite, ensure you are in the project directory and have the test file test_cron_parser.py in the same directory as the script. Run the tests using the following command:

sh
Copy code
python -m unittest test_cron_parser.py or python3 -m unittest test_cron_parse.py
Contributing
Contributions to the cron_parser project are welcome. Please feel free to submit pull requests or create issues for bugs and feature requests.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details
