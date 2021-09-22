def solution(num):
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, num + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

    return dp[num]


print(solution(int(input())))
