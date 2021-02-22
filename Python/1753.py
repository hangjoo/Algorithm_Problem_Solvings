import sys
from math import inf
from queue import PriorityQueue

v, e = list(map(int, sys.stdin.readline().split()))
start = int(input())
connect = {i: [] for i in range(1, v + 1)}
for _ in range(e):
    a, b, w = list(map(int, sys.stdin.readline().split()))
    connect[a].append((b, w))


dist = {i: inf for i in range(1, v + 1)}
dist[start] = 0

visit_q = PriorityQueue()
visit_q.put((0, start))

while not visit_q.empty():
    cur_dist, cur_node = visit_q.get()
    if cur_dist <= dist[cur_node]:
        for node, weight in connect[cur_node]:
            if cur_dist + weight < dist[node]:
                dist[node] = cur_dist + weight
                visit_q.put((dist[node], node))

for shortest in dist.values():
    if shortest != inf:
        sys.stdout.write(str(shortest) + "\n")
    else:
        sys.stdout.write("INF" + "\n")
