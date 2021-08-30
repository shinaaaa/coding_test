import itertools


def solution(orders, course):
    answer = []
    dic = {}

    for c in course:
        dic.clear()

        for order in orders:
            combinations = itertools.combinations(order, c)

            for combination in combinations:

                menu = "".join(sorted(combination, reverse=False))

                if menu in dic:
                    dic[menu] += 1
                else:
                    dic[menu] = 1

        if len(dic.items()) == 0:
            continue

        m = max(dic.values())

        for d in dic:
            if dic[d] > 1 and dic[d] == m:
                answer.append(d)
    answer.sort()
    return answer