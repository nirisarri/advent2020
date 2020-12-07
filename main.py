# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Day2.passwords
import Day1.find2020

def print_day1():
    mult = Day1.find2020.calc("Day1/input.txt", 2020, 2)
    print(mult)

    mult2 = Day1.find2020.calc("Day1/input.txt", 2020, 3)
    print(mult2)

def print_day2():
    # Use a breakpoint in the code line below to debug your script.
    Day2.passwords.calc("Day2/input.txt")
    Day2.passwords.calc2("Day2/input.txt")

def print_day3():
    from Day3.toboggan import Position, count_trees, load, analize_many
    data = load("Day3/input.txt")
    position = Position(0, 0, 31)
    p = count_trees(data, position, 3, 1)
    print(p)
    print("===========")
    # m = analize_many(data, position, [(3, 1)])
    data = load("Day3/input.txt")
    position = Position(0, 0, 31)
    m = analize_many(data, position, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    print("===========MULT===========")
    print(m)
    print("===========")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_day1()
    # print_day2()
    print_day3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
