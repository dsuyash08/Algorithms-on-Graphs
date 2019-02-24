#Uses python3

import sys
from queue import *


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    count,check  = 0,0
    while check == 0:
        check = 1
        count += 1
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                if distance[i] != 10**19 and distance[adj[i][j]] > distance[i] + cost[i][j]:
                    distance[adj[i][j]] = distance[i] + cost[i][j]                    
                    if count >=  len(adj):
                        u = adj[i][j]
                        bfs(shortest,u,adj)            
                        break
                    check = 0        
    distance[s] = 0

def bfs(reachable, i, adj):
    q = Queue(maxsize = 0)
    q.put(i)
    while not q.empty():
        t = q.get()
        for j in adj[t]:
            if reachable[j] == 1:
                reachable[j] = 0
                q.put(j)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    negCycle = shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):        
        if shortest[x] == 0:
            print('-')
        elif distance[x] == 10**19:
            print('*')
        else:
            print(distance[x])


