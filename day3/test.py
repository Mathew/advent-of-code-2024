
import unittest
from main import MUL_MATCH, Command, create_commands_from_strings, parse_commands_from_input

class CommandStringParserTest(unittest.TestCase):

    TEST_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    def test_parser(self):
        commands = parse_commands_from_input(self.TEST_INPUT, MUL_MATCH)

        self.assertEqual(commands, ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"])


class CommandStringCreatorTest(unittest.TestCase):
    TEST_INPUTS = ["mul(2,4)", "mul(5, 5)", "mul(11, 8)", "mul(8, 5)", ]

    def test_create_commands(self):
        commands = create_commands_from_strings(self.TEST_INPUTS)

        self.assertEqual(commands, [
            Command("mul", [2, 4]), Command("mul", [5, 5]), 
            Command("mul", [11, 8]), Command("mul", [8, 5])])

    def test_create_commands_operators(self):
        pass


if __name__ == "__main__":
    unittest.main()
