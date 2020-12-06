def load(file):
    f = open(file)
    data = f.readlines()
    f.close()
    return data


def count_results(the_list):
    results = 0
    for x in the_list:
        passw = Password(x)
        if passw.is_password_valid():
            results = results + 1
    return results


def count_results2(the_list):
    results = 0
    for x in the_list:
        passw = Password(x)
        if passw.is_password_valid2():
            results = results + 1
    return results


class Password:
    def __init__(self, line):
        self.line = line
        self.password = line[line.find(":") + 2:]
        self.char = line[line.find(":") - 1]
        limit = line[:line.find(":") - 2]
        self.low_limit = int(limit[:limit.find("-")])
        self.high_limit = int(limit[limit.find("-") + 1:])

    def is_password_valid(self):
        occurrences = self.password.split(self.char)
        numoccurrences = len(occurrences) - 1
        return self.low_limit <= numoccurrences <= self.high_limit

    def is_password_valid2(self):
        lowchar = self.password[self.low_limit - 1]
        hichar = self.password[self.high_limit - 1]
        b = (lowchar == self.char and hichar != self.char) or (lowchar != self.char and hichar == self.char)
        if b is True:
            template = ""
            for i in range(len(self.password)-1):
                if i == self.low_limit - 1 or i == self.high_limit - 1:
                    template = template + self.char
                else:
                    template = template + '_'
            print(self.password + template)
        return b

def calc(filename):
    the_list = load(filename)
    results = count_results(the_list)
    print("number of valid passwords:")
    print(results)


def calc2(filename):
    the_list = load(filename)
    results = count_results2(the_list)
    print("number of valid passwords:")
    print(results)
