def mult(success, values):
    if success:
        total =1
        for x in values:
            total = total * x
        return total
    else:
        return 0

def three_sums(total, expenses):
    global answer
    if len(expenses) <= 2:
        return False, []
    subtotal = expenses[0]
    remaining = total - subtotal
    sublist = expenses[1:]
    found = False
    success, partial = two_sums(remaining, sublist)
    if success:
        partial.append(subtotal)
        print(partial)
        return True, partial
    else:
        return three_sums(total, sublist)
    # for x in rest:
    #     if left + x == remaining:
    #         answer = True, [remaining, left, x]
    #         found = True
    # if found:
    #     print(answer[1])
    #     return answer
    # else:
    #     return two_sums(total, rest)

def two_sums(total, expenses):
    global answer
    if len(expenses) == 1:
        return False, []
    left = expenses[0]
    rest = expenses[1:]
    found = False
    for x in rest:
        if left + x == total:
            answer = True, [left, x]
            found = True
    if found:
        return answer
    else:
        return two_sums(total, rest)

def load(file):
    f = open(file)
    data = f.readlines()
    f.close()
    return data


def calc(filename, total, operators):
    values = []
    result = False
    the_list = load(filename)
    expenses = [int(x) for x in the_list]
    if operators == 2:
        result, values = two_sums(total, expenses)
    if operators == 3:
        result, values = three_sums(total, expenses)
    return mult(result, values)