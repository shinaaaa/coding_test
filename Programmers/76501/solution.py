def solution(absolutes, signs):
    answer = 0

    length = len(signs)

    for i in range(length):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
