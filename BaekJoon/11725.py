from collections import deque

n = int(input())
connect = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    connect[a].append(b)
    connect[b].append(a)

bfs = deque([1])
visit = {i: False for i in range(1, n + 1)}
node = {i: {"p": [], "c": []} for i in range(1, n + 1)}
while bfs:
    cur = bfs.popleft()
    visit[cur] = True
    for i in connect[cur]:
        if not visit[i]:
            node[cur]["c"].append(i)
            node[i]["p"].append(cur)
            bfs.append(i)

for i in range(2, n + 1):
    print(node[i]["p"][-1])
