from cronparser.command_handler import CommandHandler

def test_command_handler():
    command_string = "/usr/bin/find"
    handler = CommandHandler(command_string)
    assert handler.command == command_string
