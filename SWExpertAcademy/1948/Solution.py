def dayday(m):
    if(m == 1):
        result = 31
    elif(m == 2):
        result = 28
    elif(m == 3):
        result = 31
    elif(m == 4):
        result = 30
    elif(m == 5):
        result = 31
    elif(m == 6):
        result = 30
    elif(m == 7):
        result = 31
    elif(m == 8):
        result = 31
    elif(m == 9):
        result = 30
    elif(m == 10):
        result = 31
    elif(m == 11):
        result = 30
    elif(m == 12):
        result = 31
    return result


T = int(input())

for test_case in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    a2 = m2
    if(m1 == a2):
        result = d2-d1+1
    else:
        while m1 < a2:
            result += dayday(a2)
            a2 -= 1
        result = result - dayday(m2)+d2+dayday(m1)-d1+1
    print('#{} {}'.format(test_case, result))
