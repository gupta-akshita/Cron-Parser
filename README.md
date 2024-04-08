# Cron Parser

This project is a command-line application that parses a cron string and expands each field to show the times at which it will run. It supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Usage

### Setup

1. Clone the repository:

   ```bash
   git clone git@github.com:gupta-akshita/Cron-Parser.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cron_parser
   ```

3. Create and activate a virtual environment:

   ```bash
   # Create a virtual environment (if not already created)
   python -m venv venv

   or

   python3 -m venv venv

   # Activate the virtual environment
   # On macOS/Linux
   source venv/bin/activate
   # On Windows (cmd.exe)
   .\venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   or
   pip3 install -r requirements.txt
   ```

### Running the Cron Parser

To run the cron parser, execute the following command from the root directory of the project:

```bash
python -m cronparser "*/15 0 1,15 * 1-5 /usr/bin/find"
or
python3 -m cronparser "*/15 0 1,15 * 1-5 /usr/bin/find"
```

Replace `"*/15 0 1,15 * 1-5 /usr/bin/find"` with your desired cron string.

### Running the Tests

To run the tests, follow these steps:

1. Navigate to the root directory of the project where the `tests` directory is located:

   ```bash
   cd /path/to/cron_parser
   ```

2. Activate the virtual environment:

   ```bash
   # On macOS/Linux
   source venv/bin/activate
   # On Windows (cmd.exe)
   .\venv\Scripts\activate
   ```

3. Run the following command to execute all tests within the `tests` directory:

   ```bash
   pytest
   ```

This command will automatically discover and run all test files prefixed with `test_` in the `tests` directory and its subdirectories.

## Project Structure

The project structure is as follows:

```
cron_parser/
│
├── cronparser/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cron_expression.py
│   ├── field_parser.py
│   ├── command_handler.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cron_expression.py
│   ├── test_field_parser.py
│   └── test_command_handler.py
│
├── examples/
│   └── example_usage.py
│
├── README.md
├── LICENSE
└── setup.py
└── requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
