ts = int(input())

for idx in range(ts):
    size = int(input())
    print('#{}'.format(idx+1))
    pascal_triangle = [[0 for _ in range(size)] for __ in range(size)]
    for line in range(size):
        pascal_triangle[line][line] = 1
        pascal_triangle[line][0] = 1
        for i in range(line):
            pascal_triangle[line][i] = pascal_triangle[line -
                                                       1][i-1]+pascal_triangle[line-1][i]
    for line in range(size):
        for i in range(line+1):
            print(pascal_triangle[line][i], end=' ')
        print()
