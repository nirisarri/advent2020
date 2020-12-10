

class Boardingpass:
    def __init__(self, code):
        self.code = code
        self.row: int = find(code[:7], [0, 127])
        self.column: int = find(code[7:], [0, 7])
        self.seatId: int = (self.row * 8) + self.column


def get_full_map(size):
    full_map = []
    for r in range(size):
            full_map.append(r)
    return full_map

class Plane:
    def __init__(self):
        self.seats = []
        self.highest_id = 0
        self.available_seats = get_full_map(128*8)

    def populate(self, data):
        for code in data:
            b = Boardingpass(code)
            self.available_seats.remove(b.seatId)
            if b.seatId > self.highest_id:
                self.highest_id = b.seatId
            self.seats.append(b)
        return self.highest_id


def find(code, ra):
    for i in code:
        half: int = ((ra[1] - ra[0] + 1) / 2)
        if i == 'F' or i == 'L':
            ra = [ra[0], ra[1] - half]
        if i == 'B' or i == 'R':
            ra = [ra[0] + half, ra[1]]
    return ra[0]


