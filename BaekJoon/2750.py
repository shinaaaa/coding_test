# 문제 유형 : 정렬

n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    # 가장 작은 원소의 번호
    min_index = i
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    # 순서 변경
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)

# 기본 정렬 라이브러리
# n = int(input())
# array = list()

# for _ in range(n):
#     array.append(int(input()))

# array.sort()

# for i in array:
#     print(i)
