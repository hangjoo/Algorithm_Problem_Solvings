n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(n):
    for j in range(10):
        if i == 0:
            dp[0][j] = 1
        else:
            for k in range(j, 10):
                dp[i][j] += dp[i - 1][k]

print(sum(dp[-1]) % 10_007)
