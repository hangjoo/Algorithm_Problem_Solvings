n, m = map(int, input().split())


def find(cur_nums, cur_idx):
    global n, m
    if cur_idx == m:
        print(*cur_nums)
    else:
        for i in range(1, n + 1):
            if not cur_nums or i > max(cur_nums):
                cur_nums.append(i)
                find(cur_nums, cur_idx + 1)
                cur_nums.pop()


find([], 0)
