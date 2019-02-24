#Uses python3

import sys

sys.setrecursionlimit(200000)

clock = 0

def currentClock():
    global clock
    clock += 1
    return clock


def number_of_strongly_connected_components(adj):
    result = 0
    radj = [[]for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            radj[j].append(i)
    visited,visited2 = [0]*len(adj),[0]*len(adj)
    preorder, postorder = [0]*len(adj), [0]*len(adj)
    for k in range(len(radj)):
        if visited[k] == 0:
            explore(k,preorder,postorder,radj,visited)
    index = list(range(len(adj)))
    order = list(zip(index,postorder))
    order.sort(key = lambda x:x[1],reverse = True)
    for k in order:
        if visited2[k[0]] == 0:
            result += 1
            explore2(k[0],adj,visited2)
    return result

def explore2(i, adj, visited):
    visited[i] = 1
    for j in adj[i]:
        if visited[j] == 0:
            explore2(j, adj, visited)

def explore(i, preorder, postorder, adj, visited):
    preorder[i] = currentClock()
    visited[i] = 1
    for j in adj[i]:
        if visited[j] == 0:
            explore(j, preorder, postorder, adj, visited)
    postorder[i] = currentClock()

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
