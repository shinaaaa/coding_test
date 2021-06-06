import collections
import copy


def get_count_zero(maps_: list):
    map_x = len(maps_)
    map_y = len(maps_[0])
    zero_count = 0

    for x_ in range(map_x):
        for y_ in range(map_y):
            if maps_[x_][y_] == 0:
                zero_count += 1

    return zero_count


# 바이러스 전파
def spread(maps_: list, virus_: list):
    queue = collections.deque()

    # 바이러스 위치를넣음
    for x_, y_ in virus_:
        queue.append([x_, y_])

    while queue:
        qu = queue.popleft()

        # 바이러스를 이동시킬 위치
        moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for m_x, m_y in moves:
            # 이동한 바이러스 위치
            x_ = qu[0] + m_x
            y_ = qu[1] + m_y

            # 지도의 크기를 벗어나는 경우
            if len(maps_) - 1 < x_ or len(maps_[0]) - 1 < y_ or x_ < 0 or y_ < 0:
                continue
            # 벽을 만난 경우
            if maps_[x_][y_] == 1:
                continue
            # 이미 바이러스에 전염된 경우
            if maps_[x_][y_] == 2:
                continue

            maps_[x_][y_] = 2
            queue.append([x_, y_])

    return get_count_zero(maps_)


# 행렬 크기 받아옴
n, m = map(int, input().split())

# 행렬 선언
matrix = []

# 행렬에 데이터를 넣음
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 빈칸 선언
zero = []
virus = []
count = 0

# 행렬에서 빈칸, 바이러스 위치를 받아옴
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 0:
            zero.append([x, y])
        elif matrix[x][y] == 2:
            virus.append([x, y])

for x in range(len(zero) - 2):
    for y in range(x + 1, len(zero) - 1):
        for z in range(y + 1, len(zero)):
            maps = copy.deepcopy(matrix)

            x_x, x_y = zero[x]
            y_x, y_y = zero[y]
            z_x, z_y = zero[z]

            maps[x_x][x_y] = 1
            maps[y_x][y_y] = 1
            maps[z_x][z_y] = 1

            count = max(count, spread(maps, virus))

print(count)
