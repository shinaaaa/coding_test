def solution(record):
    answer = []

    log = list(item.split(" ") for item in record)
    commit = []
    name = {}

    for item in log:
        if item[0] == 'Enter':
            commit.append([item[1], '님이 들어왔습니다.'])
            name[item[1]] = item[2]
        elif item[0] == 'Leave':
            commit.append([item[1], '님이 나갔습니다.'])
        elif item[0] == 'Change':
            name[item[1]] = item[2]

    for item in commit:
        answer.append(name[item[0]] + item[1])

    return answer
