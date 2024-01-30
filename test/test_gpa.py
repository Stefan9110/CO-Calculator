import unittest

from src.points import gpa_points, points_as_percentage, required_points_for_gpa


class TestGpaRound(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(gpa_points(9500), 9.5)

    def test_zero(self):
        self.assertEqual(gpa_points(0), 0)

    def test_rounding_up(self):
        self.assertEqual(gpa_points(9250), 9.5)

    def test_rounding_down(self):
        self.assertEqual(gpa_points(9240), 9)

    def test_high_value(self):
        self.assertEqual(gpa_points(9750), 10)

    def test_high_value_rounding_down(self):
        self.assertEqual(gpa_points(9745), 9.5)


class TestPercentageComplete(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(points_as_percentage(9500), 55.88)

    def test_zero(self):
        self.assertEqual(points_as_percentage(0), 0)

    def test_rounding_up(self):
        self.assertEqual(points_as_percentage(9250), 54.41)

    def test_rounding_down(self):
        self.assertEqual(points_as_percentage(9240), 54.35)

    def test_high_value(self):
        self.assertEqual(points_as_percentage(9750), 57.35)

    def test_high_value_rounding_down(self):
        self.assertEqual(points_as_percentage(9745), 57.32)


class TestRequiredPoints(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(required_points_for_gpa(0), 0)

    def test75(self):
        self.assertEqual(required_points_for_gpa(10), 9750)

    def test25(self):
        self.assertEqual(required_points_for_gpa(9.5), 9250)

    def testRoundedGpaLow(self):
        # 9.74 rounds to 9.5 GPA which requires 9250 points to be obtained
        self.assertEqual(required_points_for_gpa(9.74), 9250)

    def testRoundedGpaHigh(self):
        # 9.75 rounds to 10 GPA which requires 9750 points to be obtained
        self.assertEqual(required_points_for_gpa(9.75), 9750)


if __name__ == '__main__':
    unittest.main()
