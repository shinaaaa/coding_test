def solution(board, moves):
    answer = 0

    depth = len(board)
    result = []

    for move in moves:
        for d in range(depth):
            # 인형을 꺼냄
            toy = board[d][move - 1]
            # 인형이 있을 경우
            if toy != 0:
                # 인형을 꺼내서 0으로 변경
                board[d][move - 1] = 0
                if len(result) > 0:
                    if result[-1] == toy:
                        result.pop()
                        answer += 1
                        break
                    else:
                        result.append(toy)
                        break
                else:
                    result.append(toy)
                    break

    return answer * 2
