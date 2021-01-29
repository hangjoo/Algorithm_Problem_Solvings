a, b, c = list(map(int, input().split()))
dp = dict()


def a_b_mod_c(a, b, c):
    if b == 1:
        return a % c
    else:
        if b not in dp.keys():
            dp[b] = (a_b_mod_c(a, b // 2, c) * a_b_mod_c(a, b - b // 2, c)) % c
        return dp[b]


print(a_b_mod_c(a, b, c))
