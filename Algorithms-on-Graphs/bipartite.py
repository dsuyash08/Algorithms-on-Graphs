#Uses python3

import sys
from queue import *

def bipartite(adj):
    visited = [0] * len(adj)
    prev = [-1]*len(adj)
    for i in range(len(adj)):
        if visited[i] == 0:
            if bfs(i,adj,visited,prev):
                return 0
    return 1

def bfs(i,adj,visited,prev):
    q = Queue(maxsize = 0)
    q.put(i)    
    visited[i] = 1
    prev[i] = 1
    while not q.empty():
        t = q.get()
        for j in adj[t]:
            if prev[j] == prev[t]:
                return True
            if visited[j] != 1:
                q.put(j)
                prev[j] = 1 - prev[t]                
                visited[j] = 1            
    return False

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
    print(bipartite(adj))
