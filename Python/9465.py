t = int(input())
for _ in range(t):
    n = int(input())
    scores = [[up, down] for up, down in zip(list(map(int, input().split())), list(map(int, input().split())))]
    dp = [[-1, -1] for _ in range(n)]

    for i in range(n):
        for j in range(2):
            # base case 1
            if i == 0:
                dp[0][j] = scores[0][j]
            # base case 2
            elif i == 1:
                dp[1][j] = scores[0][not j] + scores[1][j]
            else:
                dp[i][j] = max(dp[i - 2][j], dp[i - 2][not j], dp[i - 1][not j]) + scores[i][j]

    print(max(dp[-1][0], dp[-1][1]))
