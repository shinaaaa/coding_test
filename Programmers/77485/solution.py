def solution(rows, columns, queries):
    answer = []
    low = 0

    matrix = [[(x * columns + y) for y in range(1, columns + 1)] for x in range(rows)]

    for q in queries:
        x1 = q[0]
        y1 = q[1]
        x2 = q[2]
        y2 = q[3]

        move_horizontal = y2 - y1
        move_vertical = x2 - x1

        mx = x1 - 1
        my = y1 - 1

        # 기준 값을 임시 저장
        temp = matrix[mx][my]

        low = 0
        low = temp

        # 위쪽 좌 -> 우 이동
        for _ in range(move_horizontal):
            n = matrix[mx][my + 1]
            matrix[mx][my + 1] = temp
            temp = n
            if low > temp:
                low = temp
            my += 1

        # 우측 위 -> 아래 이동
        for _ in range(move_vertical):
            n = matrix[mx + 1][my]
            matrix[mx + 1][my] = temp
            temp = n
            if low > temp:
                low = temp
            mx += 1

        # 아래쪽 우 -> 좌 이동
        for _ in range(move_horizontal, 0, -1):
            n = matrix[mx][my - 1]
            matrix[mx][my - 1] = temp
            temp = n
            if low > temp:
                low = temp
            my -= 1

        # 좌측 아래 -> 위 이동
        for _ in range(move_vertical, 0, -1):
            n = matrix[mx - 1][my]
            matrix[mx - 1][my] = temp
            temp = n
            if low > temp:
                low = temp
            mx -= 1

        answer.append(low)

    return answer
