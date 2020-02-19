import copy

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = []
    count = 0
    for i in range(n):
        arr.append(list(map(int, input().split())))

    il = []
    result = []

    while True:
        for i in range(n):
            text = ""
            a = []
            for j in range(n-1, -1, -1):
                text += str(arr[j][i])
                a.append(arr[j][i])
            result.append(text)
            il.append(a)
        count += 1 
        if count > 2:
            break
    print(result)
    print(il)
