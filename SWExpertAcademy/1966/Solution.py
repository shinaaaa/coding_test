T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    print("#{}".format(test_case), end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print('')
