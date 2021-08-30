def solution(price, money, count):
    answer = 0

    cost = 0

    for _ in range(count):
        cost += price
        answer += cost

    if answer > money:
        answer -= money
    else:
        answer = 0

    return answer
