import re

def read_passport(lines):
    p = Passport()
    for line in lines:
        p.add_fields(line)
    return p


def reg_check(s, reg):
    r = re.match(reg, s)
    return r is not None


def check_height(hgt, ):
        r= re.match("^(\d*)cm$", hgt)
        if r is not None:
            return 150 <= int(r.group(1)) <= 193
        r = re.match("^(\d*)in$", hgt)
        if r is not None:
            return 59 <= int(r.group(1)) <= 76
        return False


class Passport:
    def __init__(self):
        self.hcl = ""
        self.eyr = ""
        self.pid = ""
        self.ecl = ""
        self.byr = ""
        self.iyr = ""
        self.hgt = ""
        self.cid = ""

    def tokenize(self, line):
        fields = line.split(" ")
        return fields

    def add_fields(self, line):
        fields = self.tokenize(line)
        for f in fields:
            field = f.split(":")
            self.__dict__[field[0]] = field[1].strip()

    def is_valid(self):
        return \
            len(self.hcl) != 0 and \
            len(self.eyr) != 0 and \
            len(self.ecl) != 0 and \
            len(self.byr) != 0 and \
            len(self.iyr) != 0 and \
            len(self.hgt) != 0 and \
            len(self.pid) != 0

    def is_valid2(self):
        a = len(self.hcl) != 0 and reg_check(self.hcl, "^#[a-fA-f0-9]{6}$")
        b = len(self.eyr) != 0 and reg_check(self.eyr, "^\d{4}$") and 2020 <= int(self.eyr) <= 2030
        c = len(self.ecl) != 0 and self.ecl in "amb blu brn gry grn hzl oth"
        d = len(self.byr) != 0 and reg_check(self.byr, "^\d{4}$") and 1920 <= int(self.byr) <= 2002
        e = len(self.iyr) != 0 and reg_check(self.iyr, "^\d{4}$") and 2010 <= int(self.iyr) <= 2020
        f = len(self.hgt) != 0 and check_height(self.hgt)
        g = len(self.pid) != 0 and reg_check(self.pid, "^\d{9}$")
        return a and b and c and d and e and f and g
        # len(self.cid) != 0
