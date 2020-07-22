# Aditya Jha

import sys

sys.setrecursionlimit(200000)

def ordering(adj, n):
    completed = [[False, False] for _ in range(n)]
    order = []
    for i in range(n):
        # if not completed[i][1]:
        #     completed[i][0] = True
        #     for a in adj[i]:
        explore(adj, i, completed, order)
            # order.append(a)
    return order

def explore(adj, x, completed, order):
    if not completed[x][0]:
        completed[x][0] = True
        for i in adj[x]:
            explore(adj, i, completed, order)
        completed[x][1] = True
        order.append(x)

def connected(adj, x, visited):
    for i in adj[x]:
        if not visited[i]:
            visited[i] = True
            connected(adj, i, visited)

def number_of_strongly_connected_components(adj, order):
    result = 0
    visited = [(False) for _ in range(n)]
    for i in range(n):
        x = order.pop()
        if not visited[x]:
            result += 1
            visited[x] = True
            connected(adj, x, visited)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjRev = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adjRev[b - 1].append(a - 1)
    order = ordering(adjRev, n)
    print(number_of_strongly_connected_components(adj, order))