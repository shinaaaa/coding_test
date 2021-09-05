import itertools
import math


# 조합
def combinations(data: list, count: int):
    return list(itertools.combinations(data, count))


# 소수 만들기
def primeNumber(data: list):
    result = 0

    for d in data:
        sum_d = sum(d)
        sqrt = math.trunc(math.sqrt(sum_d)) + 1

        isPrimeNumber = True

        for i in range(2, sqrt):
            if sum_d % i == 0:
                isPrimeNumber = False
                break

        if isPrimeNumber:
            result += 1

    return result


def solution(nums):
    return primeNumber(combinations(nums, 3))
