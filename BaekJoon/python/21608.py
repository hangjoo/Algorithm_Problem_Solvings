n = int(input())

# init.
favors = {}
for _ in range(n ** 2):
    line = list(map(int, input().split()))
    favors[line[0]] = line[1:]
orders = [i for i in favors.keys()]

board = [[-1 for _ in range(n)] for _ in range(n)]

# search.
for stud in orders:
    cand_x, cand_y = None, None
    favor_n = -1
    empty_n = -1

    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                favor_count = 0
                empty_count = 0
                for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    if 0 <= i + a < n and 0 <= j + b < n:
                        if board[i + a][j + b] in favors[stud]:
                            favor_count += 1
                        if board[i + a][j + b] == -1:
                            empty_count += 1
                if favor_count > favor_n:
                    favor_n = favor_count
                    empty_n = empty_count
                    cand_x, cand_y = i, j
                elif favor_count == favor_n and empty_count > empty_n:
                    favor_n = favor_count
                    empty_n = empty_count
                    cand_x, cand_y = i, j

    board[cand_x][cand_y] = stud

# get score.
score = 0
for i in range(n):
    for j in range(n):
        favor_count = 0
        for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if 0 <= i + a < n and 0 <= j + b < n:
                if board[i + a][j + b] in favors[board[i][j]]:
                    favor_count += 1
        if favor_count > 0:
            score += 10 ** (favor_count - 1)

print(score)
