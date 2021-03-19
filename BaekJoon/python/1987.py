import sys
input = sys.stdin.readline
print = sys.stdout.write

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

bfs_q = set()
bfs_q.add((0, 0, board[0][0]))

dist = -1

while bfs_q:
    cur_i, cur_j, cur_path = bfs_q.pop()
    dist = max(dist, len(cur_path))
    if dist == 26:
        break

    for a in range(4):
        next_i = cur_i + di[a]
        next_j = cur_j + dj[a]
        if 0 <= next_i < r and 0 <= next_j < c and board[next_i][next_j] not in cur_path:
            bfs_q.add((next_i, next_j, cur_path + board[next_i][next_j]))


print(str(dist))
