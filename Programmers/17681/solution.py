def solution(n, arr1, arr2):
    answer = []

    list1 = []
    list2 = []

    # 반복문
    for i in range(n):
        item1 = format(arr1[i], 'b')
        item2 = format(arr2[i], 'b')

        s1 = list(binary(item1, n))
        s2 = list(binary(item2, n))

        result = ''
        for j in range(n):
            if s1[j] == '0' and s2[j] == '0':
                result = result + ' '
            else:
                result = result + '#'

        answer.append(result)

    return answer


def binary(item, n):
    while len(item) < n:
        item = '0' + item
    return item