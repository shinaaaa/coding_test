T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = []
    m = 50000
    switch = 0
    while True:
        if(m < 10):
            break
        arr.append(int(n / m))
        n = n % m
        if(switch == 0):
            m = m/5
            switch = 1
        else:
            m = m/2
            switch = 0
    print('#{}'.format(test_case))
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print(' ')
