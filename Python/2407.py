n, m = list(map(int, input().split()))
cache = [[-1 for j in range(m + 1)] for i in range(n + 1)]


def nCr(n, r):
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1
    else:
        if cache[n][r] == -1:
            cache[n][r] = nCr(n - 1, r) + nCr(n - 1, r - 1)
        return cache[n][r]


print(nCr(n, m))
