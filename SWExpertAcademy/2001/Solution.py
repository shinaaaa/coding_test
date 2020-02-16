T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = []

    for i in range(n):
        li = list(map(int, input().split()))
        arr.append(li)

    for i in range(n):
        for j in range(n):
            print()
    print(arr)
