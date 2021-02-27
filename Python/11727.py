n = int(input())
cache = [0 for _ in range(n)]

cache[0] = 1
if n > 0:
    cache[1] = 3
for i in range(2, n):
    cache[i] = cache[i - 1] + 2 * cache[i - 2]

print(cache[-1] % 10_007)
