n = int(input())
cost = list(map(int, input().split()))
max_pay = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        max_pay[0] = cost[0]
    else:
        max_cost = 0
        for j in range(i):
            if max_cost < max_pay[j] + cost[i - j - 1]:
                max_cost = max_pay[j] + cost[i - j - 1]
        max_pay[i] = max(cost[i], max_cost)

print(max_pay[-1])
