from itertools import combinations
from math import inf

n = int(input())
syn = [list(map(int, input().split())) for _ in range(n)]


def synergy_score(nums: list):
    score = 0
    for num_i in nums:
        for num_j in nums:
            if num_i == num_j:
                continue
            score += syn[num_i][num_j]

    return score


min_diff = inf
kinds = combinations([i for i in range(n)], n // 2)
for kind in kinds:
    others = [i for i in range(n) if i not in kind]

    kind_score = synergy_score(kind)
    other_score = synergy_score(others)
    diff = abs(kind_score - other_score)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
