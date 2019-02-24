#Uses python3

import sys
import queue

class node:
    def __init__(self,distance,index):
        self.distance = distance
        self.index = index
    def __cmp__(self,other):
        return cmp(self.distance,other.distance)

def distance(adj, cost, s, e):
    dist = [10**19]*len(adj)
    dist[s] = 0
    q = queue.PriorityQueue()
    q.put([dist[s],s])
    while not q.empty():
        t = q.get()
        for i in range(len(adj[t[1]])):
            if dist[adj[t[1]][i]] > dist[t[1]] + cost[t[1]][i]:
                dist[adj[t[1]][i]] = dist[t[1]] + cost[t[1]][i]
                q.put([dist[adj[t[1]][i]],adj[t[1]][i]])
    if dist[e] == 10**19:
        return -1
    return dist[e]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
