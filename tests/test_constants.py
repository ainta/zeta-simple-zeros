import unittest

from zeta_simple_zeros.constants import H0, seven_point_bound, three_point_bound


class ConstantTests(unittest.TestCase):
    def test_anthropic_constant(self):
        self.assertAlmostEqual(H0, 0.6725007036794116, places=15)

    def test_three_point_bound_is_strict(self):
        epsilon = 221 / 1_000_000
        self.assertGreater(three_point_bound(epsilon), H0)
        self.assertAlmostEqual(three_point_bound(epsilon), 0.6725197671136778, places=14)

    def test_seven_point_bound(self):
        self.assertAlmostEqual(seven_point_bound(), 0.6730085279277798, places=15)


if __name__ == "__main__":
    unittest.main()
