import unittest

from main import is_report_safe, is_report_safe_dampened

class TestIsReportSafe(unittest.TestCase):

    def test_success_incrementing(self):
        self.assertTrue(is_report_safe([1, 2, 4, 7, 8]))

    def test_success_decrementing(self):
        self.assertTrue(is_report_safe([8, 7, 4, 2, 1]))

    def test_failure_out_of_range(self):
        self.assertFalse(is_report_safe([1, 2, 10, 11, 12]))
        self.assertFalse(is_report_safe([1, 10, 11, 12, 13, 14]))
        self.assertFalse(is_report_safe([12, 11, 10, 2, 1]))
        self.assertFalse(is_report_safe([14, 10, 9, 8, 7, 6]))

    def test_failure_equal_levels(self):
        self.assertFalse(is_report_safe([1, 2, 3, 4, 4, 5]))
        self.assertFalse(is_report_safe([1, 1, 2, 3, 4, 5]))

    def test_failure_decrementing_but_incrementing(self):
        self.assertFalse(is_report_safe([1, 2, 1, 4, 5]))

    def test_failure_incrementing_but_decrementing(self):
        self.assertFalse(is_report_safe([5, 4, 5, 3, 2]))

    def test_part_2_examples(self):
        self.assertTrue(is_report_safe_dampened([7, 6, 4, 2, 1]))
        self.assertFalse(is_report_safe_dampened([1, 2, 7, 8, 9]))
        self.assertFalse(is_report_safe_dampened([9, 7, 6, 2, 1]))
        self.assertTrue(is_report_safe_dampened([1, 3, 2, 4, 5]))
        self.assertTrue(is_report_safe_dampened([8, 6, 4, 4, 1]))
        self.assertTrue(is_report_safe_dampened([1, 3, 6, 7, 9]))
        self.assertTrue(is_report_safe_dampened([76, 77, 79, 82, 84, 87, 89, 95]))


if __name__ == "__main__":
    unittest.main()
