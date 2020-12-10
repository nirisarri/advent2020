import unittest

from Day5.plane import find, Plane


class MyTestCase(unittest.TestCase):
    def test_row1(self):
        self.assertEqual(find("FBFBBFF", [0, 127]), 44)

    def test_row2(self):
        self.assertEqual(find("BFFFBBF", [0, 127]), 70)

    def test_row3(self):
        self.assertEqual(find("FFFBBBF", [0, 127]), 14)

    def test_row4(self):
        self.assertEqual(find("BBFFBBF", [0, 127]), 102)

    def test_lastrow(self):
        self.assertEqual(find("BBBBBBB", [0, 127]), 127)

    def test_firstcol(self):
        self.assertEqual(find("FFFFFFF", [0, 127]), 0)

    def test_col1(self):
        self.assertEqual(find("RLR", [0, 7]), 5)

    def test_col2(self):
        self.assertEqual(find("RRR", [0, 7]), 7)

    def test_col3(self):
        self.assertEqual(find("RLL", [0, 7]), 4)

    def test_plane(self):
        p = Plane()
        self.assertEqual(p.populate(["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]), 820)

if __name__ == '__main__':
    unittest.main()
