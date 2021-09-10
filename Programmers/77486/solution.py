def sell(parent, child, amount, wallet):
    fees = amount // 10
    wallet[child] += amount - fees

    if fees != 0 and parent[child] != '-':
        return sell(parent, parent[child], fees, wallet)


def solution(enroll, referral, seller, amount):
    parent = {}
    wallet = {}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        wallet[enroll[i]] = 0

    for i in range(len(seller)):
        if amount[i] == 0:
            continue
        sell(parent, seller[i], amount[i] * 100, wallet)

    return list(wallet.values())