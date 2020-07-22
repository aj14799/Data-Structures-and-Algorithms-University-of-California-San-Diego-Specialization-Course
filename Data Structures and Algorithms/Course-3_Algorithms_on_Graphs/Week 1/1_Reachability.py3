# Aditya Jha

import sys


def reach(visited, adj, x, y):
    if not visited[x]:
        visited[x] = True
        if adj[x]:
            for i in adj[x]:
                if i == y:
                    return 1
                elif not visited[i]:
                     if reach(visited, adj, i, y):
                         return 1
    return 0


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited = [(False) for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(visited, adj, x, y))