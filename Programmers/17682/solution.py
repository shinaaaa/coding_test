def solution(dartResult):
    answer = list(dartResult)

    result = []

    for c, i in enumerate(answer):
        if i.isdigit():
            if int(i) == 0 and len(result) > 0 and result[-1] == 1 and dartResult[c - 1] == '1':
                result[-1] = 10
                continue
            else:
                result.append(int(i))
                continue

        if i == 'S':
            result[-1] = result[-1]
            continue
        elif i == 'D':
            result[-1] = result[-1] ** 2
            continue
        elif i == 'T':
            result[-1] = result[-1] ** 3
            continue
        elif i == '#':
            result[-1] = result[-1] * -1
            continue
        elif i == '*':
            result[-1] = result[-1] * 2
            if len(result) > 1:
                result[-2] = result[-2] * 2

    return sum(result)
