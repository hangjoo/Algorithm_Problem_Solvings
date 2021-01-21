from collections import deque

n = int(input())

board = [[] for _ in range(n)]
house = deque()
visit_num = []

for i in range(n):
    line = input()
    for j in range(n):
        board[i].append(int(line[j]))
        if board[i][j] == 1:
            house.append((i, j))

while house:
    visit_q = deque()
    visit_q.append(house.popleft())
    visit_count = 0

    while visit_q:
        cur_i, cur_j = visit_q.popleft()
        board[cur_i][cur_j] = 0
        visit_count += 1

        if cur_i - 1 >= 0 and board[cur_i - 1][cur_j] == 1:
            visit_q.append((cur_i - 1, cur_j))
            board[cur_i - 1][cur_j] = 0
            house.remove((cur_i - 1, cur_j))
        if cur_i + 1 < n and board[cur_i + 1][cur_j] == 1:
            visit_q.append((cur_i + 1, cur_j))
            board[cur_i + 1][cur_j] = 0
            house.remove((cur_i + 1, cur_j))
        if cur_j - 1 >= 0 and board[cur_i][cur_j - 1] == 1:
            visit_q.append((cur_i, cur_j - 1))
            board[cur_i][cur_j - 1] = 0
            house.remove((cur_i, cur_j - 1))
        if cur_j + 1 < n and board[cur_i][cur_j + 1] == 1:
            visit_q.append((cur_i, cur_j + 1))
            board[cur_i][cur_j + 1] = 0
            house.remove((cur_i, cur_j + 1))

    visit_num.append(visit_count)

print(len(visit_num))
for count in sorted(visit_num):
    print(count)
