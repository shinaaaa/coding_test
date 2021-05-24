def solution(N, stages):
    answer = []
    dic = {}

    ln = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)
        if count == 0:
            dic[i] = 0
            continue

        result = count / ln
        dic[i] = result
        ln -= count

    sic = sorted(dic.items(), reverse=True, key=lambda item: item[1])
    for key, value in sic:
        answer.append(key)

    return answer
