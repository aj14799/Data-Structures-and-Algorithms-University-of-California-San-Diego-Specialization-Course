# Aditya Jha
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]
K = 3


def print_SAT_formula():

    C, V, cnt = K*len(edges) + n, n*K, 1
    print("{0} {1}".format(C, V))

    for i in range(1, n+1):
        print("{0} {1} {2} 0".format(cnt, cnt+1, cnt+2))
        cnt += 3

    for edge in edges:
        print("{0} {1} 0".format(-((edge[0]-1)*K+1), -((edge[1]-1)*K+1)))
        print("{0} {1} 0".format(-((edge[0]-1)*K+2), -((edge[1]-1)*K+2)))
        print("{0} {1} 0".format(-((edge[0]-1)*K+3), -((edge[1]-1)*K+3)))


print_SAT_formula()
