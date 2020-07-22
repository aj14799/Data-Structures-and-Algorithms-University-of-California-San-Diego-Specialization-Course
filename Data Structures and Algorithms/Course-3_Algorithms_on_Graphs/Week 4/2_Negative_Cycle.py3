# Aditya Jha

import sys


def bellman_ford(n, adj, adjr, cost):
    dist = [(None) for _ in range(n)]

    for i in range(n):
        change_1 = 0
        for i in range(n):
            if dist[i] is None:
                dist[i] = 0
                change_1 += 1

        if change_1 == 0:
            break

        for _ in range(n - 1):
            change = 0
            for i in range(n):
                if dist[i] is not None:
                    for k in range(len(adj[i])):
                        if dist[adj[i][k]] is None:
                            dist[adj[i][k]] = dist[i] + cost[i][k]
                            change += 1
                        else:
                            dist[adj[i][k]] = min(dist[i] + cost[i][k], dist[adj[i][k]])
                            change += 1
            if change == 0:
                break




    for i in range(n):
        if dist[i] is not None:
            for k in range(len(adj[i])):
                if dist[i] + cost[i][k] < dist[adj[i][k]]:
                    return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    adjr = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adjr[b - 1].append(a - 1)
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(bellman_ford(n, adj, adjr, cost))