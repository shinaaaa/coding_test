# 문제 유형 : 해시, 배열, 구현

n = int(input())
# [3,5,7] -> set() -> {3,5,7}
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')
