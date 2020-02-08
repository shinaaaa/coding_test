def grade(idx):
    score = {
        0: 'D0',
        1: 'C-',
        2: 'C0',
        3: 'C+',
        4: 'B-',
        5: 'B0',
        6: 'B+',
        7: 'A-',
        8: 'A0',
        9: 'A+'
    }
    return score.get(idx, '{} is invalid index (0-9)'.format(idx))


T = int(input())

for test_case in (1, T+1):
    n, k = map(int, input().split())
    arr = []
    for i in range(1, n+1):
        li = list(map(int, input().split()))
        sum = li[0]*0.35 + li[1]*0.45 + li[2]*0.2
        if len(arr) != 0:
            for j in range(len(arr), -1, -1):
                if(arr[j-1][1] < sum or j == 0):
                    arr.insert(j, [i, sum])
                    break
        else:
            arr.append([i, sum])

    for i in range(len(arr)):
        if(arr[i][0] == k):
            print('#{} {}'.format(test_case, grade(i)))
            break
