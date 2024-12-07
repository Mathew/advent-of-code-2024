import unittest

from main import count_xmas, search_from_position


class TestArrayParsing(unittest.TestCase):

    # s/\(\w\)/"\1",/g
    TEST_INPUT = [
        ["M","M","M","S","X","X","M","A","S","M",],
        ["M","S","A","M","X","M","S","M","S","A",],
        ["A","M","X","S","X","M","A","A","M","M",],
        ["M","S","A","M","A","S","M","S","M","X",],
        ["X","M","A","S","A","M","X","A","M","M",],
        ["X","X","A","M","M","X","X","A","M","A",],
        ["S","M","S","M","S","A","S","X","S","S",],
        ["S","A","X","A","M","A","S","A","A","A",],
        ["M","A","M","M","M","X","M","M","M","M",],
        ["M","X","M","X","A","X","M","A","S","X",],
    ]

    def test_xmas_search(self):
        self.assertEqual(search_from_position((2, 2), self.TEST_INPUT), 0)
        self.assertEqual(search_from_position((4, 0), self.TEST_INPUT), 1)
        self.assertEqual(search_from_position((5, 9), self.TEST_INPUT), 3)
        self.assertEqual(search_from_position((1, 9), self.TEST_INPUT), 1)

    def test_count_xmas(self):
        self.assertEqual(count_xmas(self.TEST_INPUT), 18)


if __name__ == "__main__":
    unittest.main()
