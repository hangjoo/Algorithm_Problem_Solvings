class deck:
    def __init__(self):
        self.deckList = []
        self.deckSize = 0

    def pushFront(self, x: int):
        self.deckSize += 1
        self.deckList.insert(0, x)

    def pushBack(self, x: int):
        self.deckSize += 1
        self.deckList.append(x)

    def popFront(self):
        if self.deckSize == 0:
            return -1
        else:
            self.deckSize -= 1
            return self.deckList.pop(0)

    def popBack(self):
        if self.deckSize == 0:
            return -1
        else:
            self.deckSize -= 1
            return self.deckList.pop()

    def size(self):
        return self.deckSize

    def empty(self):
        return 1 if self.deckSize == 0 else 0

    def front(self):
        if self.deckSize == 0:
            return -1
        else:
            return self.deckList[0]

    def back(self):
        if self.deckSize == 0:
            return -1
        else:
            return self.deckList[-1]


cmdNum = int(input())
deckQ = deck()
for _ in range(cmdNum):
    cmd = input().split()
    if cmd[0] == "front":
        print(deckQ.front())
    elif cmd[0] == "back":
        print(deckQ.back())
    elif cmd[0] == "pop_front":
        print(deckQ.popFront())
    elif cmd[0] == "pop_back":
        print(deckQ.popBack())
    elif cmd[0] == "size":
        print(deckQ.size())
    elif cmd[0] == "empty":
        print(deckQ.empty())
    elif cmd[0] == "push_front":
        deckQ.pushFront(int(cmd[1]))
    elif cmd[0] == "push_back":
        deckQ.pushBack(int(cmd[1]))
    else:
        pass
