import unittest
import pprint

from main import Position, parse_grid, find_guard, calculate_inf_loops

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

    def test_obstacles(self):
        guard = find_guard(GRID)
        guard.walk(GRID)

        self.assertEqual(calculate_inf_loops(GRID, guard), 6)


if __name__ == "__main__":
    unittest.main()

