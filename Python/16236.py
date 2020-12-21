class bs:
    def __init__(self, board: list, sharkPos: list, fishList: list):
        self.board = board
        self.boardSize = len(board)
        self.size = 2
        self.eatCount = 0
        self.sharkPos = sharkPos  # [shark_x, shark_y]
        self.fishList = fishList  # [[fish1_x, fish1_y, fish1_size], [fish2_x, fish2_y, fish2_size], ...]

    def shortestFish(self):
        # return length if shark can eat a fish else -1

        # init phase
        visit = [[False for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        distance = [[0 for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        bfsQ = []
        bfsQ.append(self.sharkPos)
        visit[self.sharkPos[0]][self.sharkPos[1]] = True

        shortestFish = [21, 21, 400]

        while len(bfsQ) != 0:
            curPos = bfsQ.pop(0)
            visit[curPos[0]][curPos[1]] = True

            if distance[curPos[0]][curPos[1]] > shortestFish[2]:
                self.fishList.remove(shortestFish[0], shortestFish[1], self.board[shortestFish[0]][shortestFish[1]])
                self.board[self.sharkPos[0]][self.sharkPos[1]] = 0
                self.board[shortestFish[0]][shortestFish[1]] = 9
                self.sharkPos = [shortestFish[0], shortestFish[1]]
                self.eatCount += 1
                if self.size == self.eatCount and self.size < 7:
                    self.size += 1
                    self.eatCount = 0
                return shortestFish

            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if self._checkPos([curPos[0] + a, curPos[1] + b], visit):
                    distance[curPos[0] + a][curPos[1] + b] = distance[curPos[0]][curPos[1]] + 1
                    bfsQ.append([curPos[0] + a, curPos[1] + b])

                    if (
                        self.board[curPos[0] + a][curPos[1] + b] > 0
                        and self.board[curPos[0] + a][curPos[1] + b] < 7
                        and self.board[curPos[0] + a][curPos[1] + b] < self.size
                    ):
                        if distance[curPos[0] + a][curPos[1] + b] <= shortestFish[2]:
                            if curPos[0] + a < shortestFish[0]:
                                if curPos[1] + b < shortestFish[1]:
                                    shortestFish = [curPos[0] + a, curPos[1] + b, distance[curPos[0] + a][curPos[1] + b]]

        # # sorted by columns, rows, distance (orders)
        # self.fishList = sorted(self.fishList, key=lambda x: x[1])  # sorted by columns
        # self.fishList = sorted(self.fishList, key=lambda x: x[0])  # sorted by rows
        # self.fishList = sorted(self.fishList, key=lambda x: distance[x[0]][x[1]] if distance[x[0]][x[1]] > 0 else 400)  # sorted by distance

        # shortestDist = -1
        # shortestPos = [-1, -1]
        # if self.fishList:
        #     for fish in self.fishList:
        #         if fish[2] < self.size:
        #             shortestPos = [fish[0], fish[1]]
        #             shortestDist = distance[shortestPos[0]][shortestPos[1]]
        #             self.fishList.remove(fish)
        #             self.board[self.sharkPos[0]][self.sharkPos[1]] = 0
        #             self.board[shortestPos[0]][shortestPos[1]] = 9
        #             self.sharkPos = shortestPos
        #             self.eatCount += 1
        #             if self.size == self.eatCount and self.size < 7:
        #                 self.size += 1
        #                 self.eatCount = 0
        #             break
        # return shortestDist, shortestPos

    def _checkPos(self, pos: list, visit: list):
        if pos[0] >= 0 and pos[0] < self.boardSize and pos[1] >= 0 and pos[1] < self.boardSize:  # index check
            if self.board[pos[0]][pos[1]] >= 0 and self.board[pos[0]][pos[1]] <= self.size:  # board check
                if not visit[pos[0]][pos[1]]:  # visit check
                    return True
        return False


boardSize = int(input())
board = []
fishList = []
sharkPos = []
for row in range(boardSize):
    line = list(map(int, input().split()))
    board.append(line)
    for col in range(boardSize):
        if line[col] > 0 and line[col] < 7:
            fishList.append([row, col, line[col]])
        elif line[col] == 9:
            sharkPos = [row, col]
        else:
            pass

babyShark = bs(board=board, sharkPos=sharkPos, fishList=fishList)

numSum = 0
while True:
    shortestPosX, shortestPosY, shortestDist = babyShark.shortestFish()
    print("shortest Distance:", shortestDist)
    if shortestDist == -1:
        break
    numSum += shortestDist
print(numSum)