def load(file):
    f = open(file)
    data = f.readlines()
    f.close()
    return data


def count_trees(data, initial_position, move_right, move_down):
    position = initial_position
    trees = 0
    position.move(move_right, move_down)
    while position.y < len(data):
        tree = "O"
        if data[position.y][position.x] == '#':
            trees = trees + 1
            tree = "X"
        # s = "[r: {}, d: {}, t: {}]"
        # print(s.format(position.x, position.y, tree))
        position.move(move_right, move_down)
    print("------------")
    return trees

def analize_many(data, initial_position, slopes):
    multiplication = 1
    w = initial_position.max_width
    for r, d in slopes:
        trees = count_trees(data, Position(0, 0, w), r, d)
        print(trees)
        multiplication = multiplication * trees
    return multiplication

class Position:
    def __init__(self, x, y, max_width):
        self.x = x
        self.y = y
        self.max_width = max_width

    def move(self, move_right, move_down):
        self.x = self.x + move_right
        self.y = self.y + move_down
        if self.x >= self.max_width:
            self.x = self.x - self.max_width
