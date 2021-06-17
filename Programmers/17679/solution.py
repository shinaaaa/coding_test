def solution(m, n, board):
    answer = 0

    matrix = [list(item) for item in board]
    flag = True

    while flag:
        flag = False
        matrix_ = [[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                current = matrix[x][y]
                if current == "":
                    continue

                moves = [[0, 1], [1, 0], [1, 1]]
                moves_ = [[x, y]]

                for move in moves:
                    moved_x = x + move[0]
                    moved_y = y + move[1]
                    if moved_x >= m or moved_y >= n:
                        continue

                    moved = matrix[moved_x][moved_y]

                    if moved == current:
                        moves_.append([moved_x, moved_y])

                if len(moves_) == 4:
                    for move_ in moves_:
                        matrix_[move_[0]][move_[1]] = 1

        for x in range(m):
            for y in range(n):
                if matrix_[x][y] == 1:
                    matrix[x][y] = ""
                    answer += 1
                    flag = True

        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if matrix[x][y] == "":
                    for x_ in range(x - 1, -1, -1):
                        if matrix[x_][y] != "":
                            matrix[x][y] = matrix[x_][y]
                            matrix[x_][y] = ""
                            break

    return answer
