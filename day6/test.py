import unittest
import pprint

from main import Position, parse_grid, find_guard

GRID = parse_grid([
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
])

class TestGrid(unittest.TestCase):

    def test_find_guard(self):
        self.assertEqual(find_guard(GRID).position, Position(4, 6))

if __name__ == "__main__":
    unittest.main()

