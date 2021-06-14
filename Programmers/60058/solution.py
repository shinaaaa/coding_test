def reverse(u: str):
    ans = ""
    for i in range(1, len(u) - 1):
        if u[i] == "(":
            ans += ")"
        else:
            ans += "("
    return ans


def isRight(u: str):
    right = 0
    for item in u:
        if item == "(":
            right += 1
        else:
            right -= 1
        if right < 0:
            break

    if right == 0:
        return True
    else:
        return False


def solution(p):
    if p == '':
        return ''
    count = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    if isRight(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ")" + reverse(u)
