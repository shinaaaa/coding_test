def solution(lottos, win_nums):
    s_win = set(win_nums)

    index = 0
    count = 0
    while index < len(lottos):
        if lottos[index] in s_win:
            count = count + 1
        index = index + 1

    return [rank(count + lottos.count(0)), rank(count)]


def rank(count):
    if 6 <= count:
        return 1
    elif 5 == count:
        return 2
    elif 4 == count:
        return 3
    elif 3 == count:
        return 4
    elif 2 == count:
        return 5
    elif 1 >= count:
        return 6