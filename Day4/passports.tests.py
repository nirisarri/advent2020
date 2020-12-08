import unittest

from Day4.passports import Passport, read_passport, reg_check


class MyTestCase(unittest.TestCase):
    def test_parse_line_parses_fields(self):
        line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"
        fields = Passport().tokenize(line)
        self.assertEqual(len(fields), 4)

    def test_parse_has_no_spaces(self):
        line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"
        fields = Passport().tokenize(line)
        fields_with_spaces = [f for f in fields if " " in f]
        self.assertEqual(len(fields_with_spaces), 0)

    def test_passport_loads_right_fields(self):
        line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"
        passport = Passport()
        passport.add_fields(line)
        self.assertEqual(passport.ecl, "gry")
        self.assertEqual(passport.pid, "860033327")
        self.assertEqual(passport.eyr, "2020")
        self.assertEqual(passport.hcl, "#fffffd")

    def test_passport_with_many_lines_loads_right_fields(self):
        lines = ["ecl:gry pid:860033327", "eyr:2020 hcl:#fffffd"]
        passport = read_passport(lines)
        self.assertEqual(passport.ecl, "gry")
        self.assertEqual(passport.pid, "860033327")
        self.assertEqual(passport.eyr, "2020")
        self.assertEqual(passport.hcl, "#fffffd")

    def test_isValid_not_all_fields_returns_false(self):
        lines = ["ecl:gry pid:860033327", "eyr:2020 hcl:#fffffd"]
        passport = read_passport(lines)
        self.assertEqual(passport.is_valid(), False)

    def test_isValid_all_fields_returns_true(self):
        lines = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm"]
        passport = read_passport(lines)
        self.assertEqual(passport.is_valid(), True)

    def test_isValid_all_fields_but_pid_returns_true(self):
        lines = ["hcl:#ae17e1 iyr:2013", "eyr:2024", "ecl:brn", "pid:760753108", "byr:1931", "hgt:179cm"]
        passport = read_passport(lines)
        self.assertEqual(passport.is_valid(), True)

    def test_regCheck(self):
        self.assertEqual(reg_check("1986", "^\d\d\d\d$"), True)

    def test_all(self):
        data = '''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''.split("\n")
        passport = Passport()
        valid_passports: int = 0
        for line in data:
            if len(line) != 0:
                passport.add_fields(line)
            else:
                if passport.is_valid():
                    valid_passports = valid_passports + 1
                passport = Passport()
        self.assertEqual(valid_passports, 2)


if __name__ == '__main__':
    unittest.main()
