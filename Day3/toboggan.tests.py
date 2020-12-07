import unittest

from Day3.toboggan import count_trees, Position, analize_many


class MyTestCase(unittest.TestCase):
    def test_count2lines(self):
        data = [
            "..##.......",
            "#...#...#.."]
        position = Position(0, 0, 11)
        p = count_trees(data, position, 3, 1)
        self.assertEqual(p, 0)

    def test_count2lines_hit(self):
        data = [
            "..##.......",
            "#...#...#.."]
        position = Position(0, 0, 11)
        p = count_trees(data, position, 4, 1)
        self.assertEqual(p, 1)

    def test_count_wrap_hit(self):
        data = [
            "..##.......",
            "#...#...#.."]
        position = Position(0, 0, 11)
        p = count_trees(data, position, 15, 1)
        self.assertEqual(p, 1)

    def test_count_many_lines(self):
        data = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]
        position = Position(0, 0, 11)
        p = count_trees(data, position, 11, 1)
        self.assertEqual(p, 3)

    def test_analyze_many_lines(self):
        data = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]
        p = analize_many(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
        print("================")
        print(p)
        self.assertEqual(p, 336)


    def test_count_many_lines2(self):
        data = [
".#...#.......#...#...#.#.#.....",
"####.....#.#..#...#...........#",
".....#...........#......#....#.",
"......#..#......#.#..#...##.#.#",
"............#......#...........",
"...........#.#.#....#.......##.",
"....#.......#..............#...",
"........##...#.#.....##...##.#.",
".#.#.....##................##..",
".##................##..#...##..",
"....#...###...##.........#....#",
".##......#.........#...........",
"...#.#.#....#....#...#...##...#",
"..#....##...#..#.#..#.....#.#.."
]
        position = Position(0, 0, len(data[0]))
        p = count_trees(data, position, 3, 1)
        self.assertEqual(p, 10)


if __name__ == '__main__':
    unittest.main()
