import sys
from math import inf
from queue import PriorityQueue

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
connect = {node: [] for node in range(1, n + 1)}

for _ in range(m):
    src_node, tgt_node, weight = map(int, sys.stdin.readline().split())
    connect[src_node].append((tgt_node, weight))

src, dst = map(int, sys.stdin.readline().split())

dist = {node: inf for node in range(1, n + 1)}
dist[src] = 0

pq = PriorityQueue()
pq.put([dist[src], src])

while not pq.empty():
    cur_dist, cur_node = pq.get()
    if cur_dist <= dist[cur_node]:
        for node, weight in connect[cur_node]:
            if cur_dist + weight < dist[node]:
                dist[node] = cur_dist + weight
                pq.put([dist[node], node])

sys.stdout.write(str(dist[dst]) + "\n")
