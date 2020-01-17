""" 문제 유형 : 스택, 그리디 """

n = int(input())

count = 1
stack = []
result = []

""" 데이더 개수만큼 반복 """
for i in range(1, n+1):
    data = int(input())
    """ 입력 받은 데이터에 도달할 때까지 삽입 """
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    """ 스택의 최상위 원소가 데이터와 같을 떄 출력 """
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    """ 불가능한 경우 """
    else:
        print('NO')
        exit(0)

""" 가능한 경우 """
print('\n' .join(result))
