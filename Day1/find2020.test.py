import unittest

from Day1 import find2020


class MyTestCase(unittest.TestCase):
    def test_success_at_start(self):
        result = find2020.two_sums(2020, [2010, 10, 67])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_success_at_end(self):
        result = find2020.two_sums(2020, [20, 10, 2010])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_three_success_at_end(self):
        result = find2020.three_sums(2020, [10, 10, 2000])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_three_success_at_end(self):
        result = find2020.three_sums(2020, [2000, 4000, 12, 8, 20])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_success_two_values(self):
        result = find2020.two_sums(2020,[2010, 10])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_success_at_start_and_end(self):
        result = find2020.two_sums(2020,[2010, 6, 7, 8, 9, 0, 10])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_success_at_middle_and_end(self):
        result = find2020.two_sums(2020,[6, 7, 8, 2010, 9, 0, 10])
        (success, sumands) = result
        self.assertEqual(success, True)
        self.assertEqual(sum(sumands), 2020)

    def test_mult_return_right(self):
        s, sumands = find2020.two_sums(2020,[1721, 979, 366, 299, 675, 1456])
        mult = find2020.mult(s, sumands)
        self.assertEqual(mult, 514579)

    def test_mult3_return_right(self):
        s, sumands = find2020.three_sums(2020,[1721, 979, 366, 299, 675, 1456])
        mult = find2020.mult(s, sumands)
        self.assertEqual(mult, 241861950)

    def test_readlist(self):
        expenses = find2020.load("input.txt")
        self.assertEqual(type(expenses), list)
        self.assertGreater(len(expenses), 20)

    def test_main(self):
        mult = find2020.calc("input.txt", 2020, 2)
        print (mult)

    def test_main_three(selfself):
        mult = find2020.calc("input.txt", 2020, 3)
        print (mult)

if __name__ == '__main__':
    unittest.main()
