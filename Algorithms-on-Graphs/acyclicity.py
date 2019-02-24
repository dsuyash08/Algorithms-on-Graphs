#Uses python3

import sys

check = False

def acyclic(adj):
    visited = [0]*len(adj)
    for i in range(len(adj)):
        if visited[i] == 0:
            explore(i,adj,visited,[])
            if check :
                return 1
    return 0

def explore(i,adj,visited,lists):
    global check    
    visited[i] = 1
    lists.append(i)
    for j in adj[i]:
        if j in lists:
            check = True
        if visited[j] == 0:
            explore(j,adj,visited,lists)
    lists.pop()


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
