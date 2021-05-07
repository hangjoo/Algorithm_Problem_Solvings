# init.
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def get_next(cur_a, cur_b, cur_d, rot_i):
    next_d = (cur_d + rot_i) % 4
    a, b = direction[next_d]
    next_a, next_b = cur_a + a, cur_b + b

    return next_a, next_b, next_d


# simulate.
clean_count = 0
cur_a, cur_b, cur_d = r, c, d
while True:
    # step 1.
    if board[cur_a][cur_b] == 0:
        board[cur_a][cur_b] = 2
        clean_count += 1

    # step 2.
    for i in range(1, 5):
        is_step = False
        next_a, next_b, next_d = get_next(cur_a, cur_b, cur_d, -i)
        if 0 <= next_a < n and 0 <= next_b < m and board[next_a][next_b] == 0:
            cur_a, cur_b, cur_d = next_a, next_b, next_d
            is_step = True
            break

    if not is_step:
        next_a, next_b, next_d = get_next(cur_a, cur_b, cur_d, 2)
        if not 0 <= next_a < n or not 0 <= next_b < m or board[next_a][next_b] == 1:
            break
        else:
            cur_a, cur_b, cur_d = next_a, next_b, cur_d

print(clean_count)
