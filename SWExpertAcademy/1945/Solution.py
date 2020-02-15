T = int(input())

for test_case in range(1, T+1):
    num = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while True:
        if(num % 2 == 0):
            num = num/2
            a += 1
        else:
            break

    while True:
        if(num % 3 == 0):
            num = num/3
            b += 1
        else:
            break

    while True:
        if(num % 5 == 0):
            num = num/5
            c += 1
        else:
            break

    while True:
        if(num % 7 == 0):
            num = num/7
            d += 1
        else:
            break

    while True:
        if(num % 11 == 0):
            num = num/11
            e += 1
        else:
            break
    print('#{} {} {} {} {} {}'.format(test_case, a, b, c, d, e))
