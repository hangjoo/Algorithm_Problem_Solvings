n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))


def find(cur_nums, cur_idx):
    global n, m
    if cur_idx == m:
        print(*cur_nums)
    else:
        for num in nums:
            if num not in cur_nums:
                cur_nums.append(num)
                find(cur_nums, cur_idx + 1)
                cur_nums.pop()


find([], 0)
