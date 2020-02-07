T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    arr.remove(max(arr))
    arr.remove(min(arr))
    sum(arr)
    result = 0
    if(sum(arr) % len(arr) >= 4):
        result = int(sum(arr)/len(arr))+1
    else:
        result = int(sum(arr)/len(arr))
    print('#', test_case, ' ', result)
