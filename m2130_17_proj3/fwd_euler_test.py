#!/usr/bin/env python
import unittest
from fwd_euler import *


class FwdEulerTest(unittest.TestCase):

    def test_fwd_euler_domain_discretization(self):
        expected = [0, 1, 2, 3, 4]
        x0 = 0
        h = 1
        N = 5
        computed = disc_domain(x0, h, N)
        self.assertEqual(expected, computed)


if __name__ == '__main__':
    unittest.main()
