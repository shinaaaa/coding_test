T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    print('#{}'.format(test_case))
    arr = []
    for i in range(n):
        text, num = map(str, input().split())
        arr.append([text, num])
    cc = 1
    for i in range(n):
        for _ in range(int(arr[i][1])):
            if(cc < 10):
                print(arr[i][0], end='')
                cc += 1
            else:
                print(arr[i][0])
                cc = 1
    print('')
