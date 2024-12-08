import unittest

from main import is_printing_ordered, group_orderings



TEST_ORDERINGS = (
    (47, 53),
    (97, 13),
    (97, 61),
    (97, 47),
    (75, 29),
    (61, 13),
    (75, 53),
    (29, 13),
    (97, 29),
    (53, 29),
    (61, 53),
    (97, 53),
    (61, 29),
    (47, 13),
    (75, 47),
    (97, 75),
    (47, 61),
    (75, 61),
    (47, 29),
    (75, 13),
    (53, 13),
)

TEST_PRINTINGS = (
    (75,47,61,53,29), 
    (97,61,53,29,13), 
    (75,29,13      ), 
    (75,97,47,61,53), 
    (61,13,29      ), 
    (97,13,75,29,47), 
)

class TestOrdering(unittest.TestCase):

    grouped_ordering = {
        47: [53, 13, 61, 29, ], 
        97: [13, 61, 47, 29, 53, 75, ],
        75: [29, 53, 47, 61, 13, ],
        61: [13, 53, 29, ],
        29: [13, ],
        53: [29, 13, ], 
    }

    def test_group_orderings(self):
        self.assertEqual(self.grouped_ordering.items(), group_orderings(TEST_ORDERINGS).items())

    def test_is_printing_ordered(self):
        self.assertTrue(is_printing_ordered(self.grouped_ordering, TEST_PRINTINGS[0]))
        self.assertTrue(is_printing_ordered(self.grouped_ordering, TEST_PRINTINGS[1]))
        self.assertTrue(is_printing_ordered(self.grouped_ordering, TEST_PRINTINGS[2]))
        self.assertFalse(is_printing_ordered(self.grouped_ordering, TEST_PRINTINGS[3]))
        self.assertFalse(is_printing_ordered(self.grouped_ordering, TEST_PRINTINGS[4]))
        self.assertFalse(is_printing_ordered(self.grouped_ordering, TEST_PRINTINGS[5]))


if __name__ == "__main__":
    unittest.main()

