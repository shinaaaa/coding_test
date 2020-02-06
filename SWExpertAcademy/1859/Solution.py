T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split(" ")))

    result = 0

    for i in range(0, num):
        MAX = 0
        for j in range(num-1, i, -1):
            # print('arr[i] : ', arr[i], ' arr[j] : ', arr[j])
            if(MAX < arr[j]):
                MAX = arr[j]
        if(MAX > arr[i]):
            result += MAX - arr[i]
            # print('MAX : ', MAX, ' arr[i] : ', arr[i])
    print('#', test_case, ' ', result)
