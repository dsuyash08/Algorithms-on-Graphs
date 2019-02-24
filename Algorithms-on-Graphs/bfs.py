#Uses python3

import sys
from queue import *

def distance(adj, s, e):
    visited = [0] * len(adj)
    dist = [-1]*len(adj)
    dist[s] = 0
    bfs(s,adj,visited,dist)
    return dist[e]

def bfs(i,adj,visited,dist):
    q = Queue(maxsize = 0)
    q.put(i)  
    while not q.empty():
        t = q.get()
        for j in adj[t]:
            if dist[j] == -1:
                q.put(j)
                dist[j] = dist[t] + 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
