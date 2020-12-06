import unittest

from Day2.passwords import Password, count_results, count_results2


class MyTestCase(unittest.TestCase):
    def test_loads_password(self):
        p = Password("1-3 a: abcde")
        self.assertEqual('abcde', p.password)

    def test_loads_char(self):
        p = Password("1-3 a: abcde")
        self.assertEqual('a', p.char)

    def test_loads_low_limit(self):
        p = Password("1-3 a: abcde")
        self.assertEqual(1, p.low_limit)

    def test_loads_high_limit(self):
        p = Password("1-3 a: abcde")
        self.assertEqual(3, p.high_limit)

    def test_loads_limit2(self):
        p = Password("10-30 a: abcde")
        self.assertEqual(10, p.low_limit)
        self.assertEqual(30, p.high_limit)

    def test_check_password_succeeds(self):
        p = Password("1-3 a: abcde")
        self.assertEqual(True, p.is_password_valid())

    def test_check_password_fails(self):
        p = Password("1-3 g: abcdeaaa")
        self.assertEqual(False, p.is_password_valid())

    def test_check_password2_succeeds(self):
        p = Password("2-3 a: bba")
        self.assertEqual(True, p.is_password_valid2())

    def test_check_password2_fails(self):
        p = Password("1-3 b: cdefg")
        self.assertEqual(False, p.is_password_valid2())
    #
    # def test_check_password_fails2(self):
    #     p = Password("1-3 z: abcdeaaa")
    #     self.assertEqual(False, p.is_password_valid())

    def test_count_results_sample(self):
        p = count_results(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])
        self.assertEqual(p, 2)

    def test_count_results_sample2(self):
        p = count_results(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: cc"])
        self.assertEqual(p, 2)

    def test_count_results2_sample(self):
        p = count_results2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])
        self.assertEqual(p, 2)

    def test_count_results2_sample2(self):
        p = count_results2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: cc"])
        self.assertEqual(p, 1)


if __name__ == '__main__':
    unittest.main()
