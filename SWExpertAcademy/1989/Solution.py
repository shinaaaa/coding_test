T = int(input())
 
for test_case in range(1, T + 1):
    text = str(input())
    length = len(text)
    result = 1
    for i in range(length):
        if(text[i] != text[-i-1]):
            result = 0
            break
    print('#{} {}'.format(test_case, result))
