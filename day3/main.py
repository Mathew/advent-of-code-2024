import operator
import re

MUL_MATCH = "(mul\([0-9]+,[0-9]+\))"
OPERATOR_MATCH = "((?:mul|don\'t|do)\((?:[0-9]+,[0-9]+)?\))"

class Command:
    command: str
    arguments: list[int]

    def __init__(self, command, arguments):
        self.command = command
        self.arguments = arguments

    def __eq__(self, other):
        return self.command == other.command and self.arguments == other.arguments

    def calculate(self):
        if self.command == "mul":
            return operator.mul(*self.arguments)

        return 0

def calculate_commands_tracker(commands):
    track = True
    sum = 0
    for c in commands:
        if c.command == "do":
            track = True
        elif c.command == "don\'t":
            track = False
        else:
            if track:
                sum += c.calculate()

    return sum


def parse_commands_from_input(input: str, pattern: str) -> list[str]:
    return re.findall(pattern, input)

def create_commands_from_strings(command_strings: list[str]) -> list[Command]:
    commands = []
    for r in command_strings:
        command, rem = r.split("(")
        if command == "mul":
            rem, _ = rem.split(")")
            args = rem.split(",")
            args = [int(a) for a in args]

            commands.append(Command(command, args))
        else:
            commands.append(Command(command, []))

    return commands


def load_input() -> str:
    input = []
    with open("input.csv") as f:
        for line in f.readlines():
            input.append(line)

    return ("").join(input)

def part_one(input) -> int:
    command_strings = parse_commands_from_input(input, MUL_MATCH)
    print(command_strings)
    commands = create_commands_from_strings(command_strings)

    sum = 0
    for c in commands:
        sum += c.calculate()

    return sum

def part_two(input) -> int:
    command_strings = parse_commands_from_input(input, OPERATOR_MATCH)
    commands = create_commands_from_strings(command_strings)

    return calculate_commands_tracker(commands)


def main():
    input = load_input()
    print(part_one(input))
    print(part_two(input))


if __name__ == "__main__":
    main()
