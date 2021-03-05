import sys
from collections import deque

# list의 pop()은 O(n)의 시간복잡도를 갖고,
# collections의 deque의 pop() 또는 popleft()는 O(1)의 시간복잡도를 갖는다.
# 그래서 list를 사용하여 bfs를 구현하면 시간초과가 뜬다..

m, n = list(map(int, sys.stdin.readline().split()))
tomato_container = []
bfs_q = deque()
max_day = 0
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tomato_container.append(row)
    for j in range(m):
        if row[j] == 1:
            bfs_q.append((i, j))

while bfs_q:
    cur_i, cur_j = bfs_q.popleft()

    if cur_i - 1 >= 0 and tomato_container[cur_i - 1][cur_j] == 0:
        bfs_q.append((cur_i - 1, cur_j))
        tomato_container[cur_i - 1][cur_j] = tomato_container[cur_i][cur_j] + 1
    if cur_i + 1 < n and tomato_container[cur_i + 1][cur_j] == 0:
        bfs_q.append((cur_i + 1, cur_j))
        tomato_container[cur_i + 1][cur_j] = tomato_container[cur_i][cur_j] + 1
    if cur_j - 1 >= 0 and tomato_container[cur_i][cur_j - 1] == 0:
        bfs_q.append((cur_i, cur_j - 1))
        tomato_container[cur_i][cur_j - 1] = tomato_container[cur_i][cur_j] + 1
    if cur_j + 1 < m and tomato_container[cur_i][cur_j + 1] == 0:
        bfs_q.append((cur_i, cur_j + 1))
        tomato_container[cur_i][cur_j + 1] = tomato_container[cur_i][cur_j] + 1

    if tomato_container[cur_i][cur_j] > max_day:
        max_day = tomato_container[cur_i][cur_j]

empty = False
for row in tomato_container:
    if 0 in row:
        empty = True
        break

if empty:
    sys.stdout.write(str(-1) + "\n")
else:
    sys.stdout.write(str(max_day - 1) + "\n")
