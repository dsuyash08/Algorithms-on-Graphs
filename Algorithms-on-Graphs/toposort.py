#Uses python3

import sys
clock = 0

def dfs(adj, used, preorder, x, postorder):
    global clock
    clock += 1
    preorder[x] = clock
    used[x] = 1
    for i in adj[x]:
        if(used[i] == 0):  
            dfs(adj,used,preorder,i,postorder)
    clock += 1
    postorder[x] = clock
    pass


def toposort(adj):
    used = [0] * len(adj)
    preorder = [0]*len(adj)  
    postorder = [0]*len(adj)
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(adj,used,preorder,i,postorder)
    order = []
    for i in range(len(adj)):
        order.append([i,postorder[i]])
    order.sort(key = lambda x:x[1],reverse = True)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x[0] + 1, end=' ')

