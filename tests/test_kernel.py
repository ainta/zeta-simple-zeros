import unittest

from flint import arb

from zeta_simple_zeros.kernel import (
    RangeMinimum,
    configure_arb,
    kernel_constants,
    normalized_kernel,
)


class KernelTests(unittest.TestCase):
    def setUp(self):
        configure_arb(128)

    def test_normalization(self):
        value = normalized_kernel(arb(0), kernel_constants())
        self.assertTrue(value.contains(arb(1)))

    def test_evenness(self):
        constants = kernel_constants()
        positive = normalized_kernel(arb("1.125"), constants)
        negative = normalized_kernel(arb("-1.125"), constants)
        self.assertTrue(positive.overlaps(negative))

    def test_range_minimum(self):
        table = RangeMinimum([3.0, 2.0, 4.0, 1.0, 5.0])
        self.assertEqual(table.query(0, 2), 2.0)
        self.assertEqual(table.query(2, 4), 1.0)
        self.assertEqual(table.query(3, 3), 1.0)


if __name__ == "__main__":
    unittest.main()
