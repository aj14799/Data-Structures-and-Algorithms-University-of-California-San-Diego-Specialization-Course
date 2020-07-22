# Aditya Jha
import sys


def number_of_components(n, visited, adj):
    result = 0
    for i in range(n):
        if not visited[i]:
            result += 1
            visited[i] = True
            for node in adj[i]:
                if not visited[node]:
                    connected_comp(visited, node, adj)

    return result

def connected_comp(visited, x, adj):
    visited[x] = True
    for node in adj[x]:
        if not visited[node]:
            connected_comp(visited, node, adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [(0) for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(n, visited, adj))