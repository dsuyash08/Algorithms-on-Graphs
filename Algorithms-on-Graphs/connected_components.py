#Uses python3

import sys


def number_of_components(adj):
    result = 0
    visited = [0]*len(adj)
    for i in range(len(adj)):
        if visited[i] != 1:
            connected(i,adj,visited)
            result += 1
    return result

def connected(n,adj,visited):
    s = []
    s.append(n)
    while len(s) > 0:
        t = s.pop()
        visited[t] = 1
        for i in adj[t]:
            if visited[i] == 0:
                s.append(i)


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
    print(number_of_components(adj))
