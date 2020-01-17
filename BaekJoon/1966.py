# 문제 유형 : 큐, 구현, 그리디

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))

    # enumerate : 배열의 순서와 값을 같이 출력
    # idx 가 순서를 나타냄 [(2,0), (1,1), (4,2)]

    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
