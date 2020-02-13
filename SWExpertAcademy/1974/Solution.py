T = int(input())

for test_case in range(1, T+1):
    arr = []
    li = []
    result = 1
    for i in range(9):
        li = list(map(int, input().split()))
        arr.append(li)

    for i in range(9):
        arrlist = [0]
        for j in range(9):
            if(arrlist.count(arr[i][j]) > 0):
                result = 0
                break
            else:
                arrlist.append(arr[i][j])
    for i in range(9):
        arrlist = [0]
        for j in range(9):
            if(arrlist.count(arr[j][i]) > 0):
                result = 0
            else:
                arrlist.append(arr[j][i])
    for i in range(0, 9, +3):
        arrlist = [0]
        for j in range(3):
            for k in range(3):
                if(arrlist.count(arr[j+i][k]) > 0):
                    result = 0
                    break
                else:
                    arrlist.append(arr[j+i][k])
    print('#{} {}'.format(test_case, result))
