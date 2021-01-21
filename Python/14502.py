from collections import deque
from copy import deepcopy

n, m = list(map(int, input().split()))

board = []
empty_space = deque()
infect_queue = deque()
safe_area = deque()

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 2:
            infect_queue.append((i, j))
        if board[i][j] == 0:
            empty_space.append((i, j))

for a in range(len(empty_space) - 2):
    board[empty_space[a][0]][empty_space[a][1]] = 1
    for b in range(a + 1, len(empty_space) - 1):
        board[empty_space[b][0]][empty_space[b][1]] = 1
        for c in range(b + 1, len(empty_space)):
            board[empty_space[c][0]][empty_space[c][1]] = 1

            cur_board = deepcopy(board)
            cur_queue = deepcopy(infect_queue)
            while cur_queue:
                cur_n, cur_m = cur_queue.popleft()
                if cur_n - 1 >= 0 and cur_board[cur_n - 1][cur_m] == 0:
                    cur_queue.append((cur_n - 1, cur_m))
                    cur_board[cur_n - 1][cur_m] = 2
                if cur_n + 1 < n and cur_board[cur_n + 1][cur_m] == 0:
                    cur_queue.append((cur_n + 1, cur_m))
                    cur_board[cur_n + 1][cur_m] = 2
                if cur_m - 1 >= 0 and cur_board[cur_n][cur_m - 1] == 0:
                    cur_queue.append((cur_n, cur_m - 1))
                    cur_board[cur_n][cur_m - 1] = 2
                if cur_m + 1 < m and cur_board[cur_n][cur_m + 1] == 0:
                    cur_queue.append((cur_n, cur_m + 1))
                    cur_board[cur_n][cur_m + 1] = 2

            area_count = 0
            for row in cur_board:
                area_count += row.count(0)
            safe_area.append(area_count)

            board[empty_space[c][0]][empty_space[c][1]] = 0
        board[empty_space[b][0]][empty_space[b][1]] = 0
    board[empty_space[a][0]][empty_space[a][1]] = 0

print(max(safe_area))
