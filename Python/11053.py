n = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if seq[i] > seq[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))
