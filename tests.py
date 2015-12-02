# Reference: https://docs.python.org/library/unittest

import unittest

import primes


class PrimeTest(unittest.TestCase):

    def test_10(self):
        self.assertEqual(primes.primes(10), [1, 2, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()
