def solution(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = map(int, input().split())
        for j in range(1, k + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    return dp[n][k]


n, k = map(int, input().split())
print(solution(n, k))
