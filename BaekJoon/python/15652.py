n, m = map(int, input().split())


def choose(idx, goal, nums):
    global n
    if idx == goal:
        print(*nums)
    elif idx < goal:
        start = 1 if not nums else nums[-1]
        for i in range(start, n + 1):
            nums.append(i)
            choose(idx + 1, goal, nums)
            nums.pop()


choose(0, m, [])
