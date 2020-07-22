# Aditya Jha

import sys

def ordering(adj, n):
    completed = [(False) for _ in range(n)]
    order = []
    for i in range(n):
        explore(adj, i, completed, order)
    return order

def explore(adj, x, completed, order):
    if not completed[x]:
        for i in adj[x]:
            explore(adj, i, completed, order)
        completed[x] = True
        order.append(x)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = ordering(adj, n)
    for x in range(n):
        print(order.pop() + 1, end=' ')

