n = int(input())
cost = list(map(int, input().split()))
count = [0 for _ in range(n)]
cpc = [cost[i] / (i + 1) for i in range(n)]

total = 0
left = n
while left > 0:
    idx = cpc.index(max(cpc[:left]))
    count[idx] += left // (idx + 1)
    left -= count[idx] * (idx + 1)
    total += cost[idx] * count[idx]
    cpc[idx] = 0
    print(f"{idx + 1} card pack was bought {count[idx]} times.")
    print(f"{left} cards left.")
    print(f"{cost[idx] * count[idx]} paid.")
    print()

print(total)
