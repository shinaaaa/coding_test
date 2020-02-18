T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    x = 0
    y = 0
    switch = 0
    MAX = 0

    while True:
        value = 0
        if(switch == 1):
            y += 1
            switch = 0
            if(y == n-m+1):
                break

        for i in range(y, m+y):
            for j in range(x, m+x):
                value += arr[i][j]

        if(MAX < value):
            MAX = value

        if(switch == 0):
            x += 1
            if(x == n-m+1):
                x = 0
                switch = 1
    print('#{} {}'.format(test_case, MAX))
