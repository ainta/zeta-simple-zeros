import unittest

from zeta_simple_zeros.verify_three import verify_three


class ThreePointCertificateTests(unittest.TestCase):
    def test_full_three_point_certificate(self):
        report = verify_three()
        self.assertTrue(report.verified)
        self.assertGreater(report.nodes, 0)
        self.assertEqual(report.pruned, report.splits + 1)


if __name__ == "__main__":
    unittest.main()
