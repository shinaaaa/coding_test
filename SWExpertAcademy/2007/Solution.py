T = int(input())

for test_case in range(1, T + 1):
    text = str(input())
    t1 = ''
    for i in range(1, len(text)):
        if(text[0:i] == text[i:i*2]):
            t1 = text[0:i]
            break
    print('#{} {}'.format(test_case, len(t1)))
