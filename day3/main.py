from itertools import chain
import operator
import re

class Command:
    command: str
    arguments: list[int]

    def __init__(self, command, arguments):
        self.command = command
        self.arguments = arguments

    def __eq__(self, other):
        return self.command == other.command and self.arguments == other.arguments

    def calculate(self):
        return operator.mul(*self.arguments)

def parse_commands_from_input(input: str) -> list[str]:
    pattern = "(mul\([0-9]+,[0-9]+\))"
    return re.findall(pattern, input)

def create_commands_from_strings(command_strings: list[str]) -> list[Command]:
    commands = []
    for r in command_strings:
        command, rem = r.split("(")
        rem, _ = rem.split(")")
        args = rem.split(",")
        args = [int(a) for a in args]

        commands.append(Command(command, args))

    return commands


def load_input() -> str:
    input = []
    with open("input.csv") as f:
        for line in f.readlines():
            input.append(line)

    return ("").join(input)

def main():
    input = load_input()
    command_strings = parse_commands_from_input(input)
    commands = create_commands_from_strings(command_strings)

    sum = 0
    for c in commands:
        sum += c.calculate()

    print(sum)


if __name__ == "__main__":
    main()
