ts = int(input())
for _ in range(1, ts+1):
    size = int(input().strip())
    world = [list(input().strip().split()) for row in range(size)]
    turn_90 = [['' for col in range(size)] for row in range(size)]
    turn_180 = [['' for col in range(size)] for row in range(size)]
    turn_270 = [['' for col in range(size)] for row in range(size)]
    for i in range(size):
        for j in range(size):
            turn_90[j][-1-i] = world[i][j]
            turn_180[-1-i][-1-j] = world[i][j]
            turn_270[-1-j][i] = world[i][j]
    print('#{}'.format(_))
    for i in range(size):
        print(''.join(turn_90[i]), end=' ')
        print(''.join(turn_180[i]), end=' ')
        print(''.join(turn_270[i]))
