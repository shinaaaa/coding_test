T = int(input())

for test_case in range(1, T+1):
    t1, m1, t2, m2 = map(int, input().split())

    m = m1 + m2
    t = t1 + t2

    if(m >= 60):
        m -= 60
        if(m >= 60):
            m -= 60
            t += 1
        t += 1
    if(t >= 12):
        t -= 12
    print('#{} {} {}'.format(test_case, t, m))
