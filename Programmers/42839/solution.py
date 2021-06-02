import itertools
import math


def is_prime(num):
    p = int(math.sqrt(num) + 1)
    for i in range(2, p):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    permutations = []
    for l in range(1, len(numbers) + 1):
        li = list(itertools.permutations(list(numbers), l))

        for r in range(len(li)):
            num = int(''.join(li[r]))
            if num > 1:
                if is_prime(num):
                    if permutations.count(num) == 0:
                        permutations.append(num)

    return len(permutations)