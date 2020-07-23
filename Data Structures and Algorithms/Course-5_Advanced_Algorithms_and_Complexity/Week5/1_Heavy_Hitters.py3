# Aditya Jha

import sys
import statistics as stat
import math
import numpy as np



class hash_function:
    def __init__(self, a, b, p, m):
        self.a = a
        self.b = b
        self.p = p
        self.m = m

    def hash(self, x):
        return int(((self.a * x + self.b) % self.p) % self.m)

class sign_function:
    def __init__(self):
        self.hf = hash_function(np.random.uniform(10, 50), np.random.uniform(50, 100), 10e5 + 19, 1000)

    def hash(self, x):
        return 1 if self.hf.hash(x) > 500 else -1

class count_sketch:
    def __init__(self, n):
        self.b = int(math.log(n) * 1500)
        self.t = int(math.log(n) + 1)
        self.data = [[0] * self.b ] * self.t
        self.ith_data = [0] * self.t
        self.funcs = [(hash_function(np.random.uniform(50, 100), np.random.uniform(10, 50),
                       10e8 + 19, self.b), sign_function()) for i in range(0, self.t) ]

    def update(self, i, frq = 1):
        for j in range(0, self.t):
            self.data[j][self.funcs[j][0].hash(i)] += self.funcs[j][1].hash(i) * frq

    def estimate(self, i):
        for j in range(0, self.t):
            self.ith_data[j] = self.data[j][self.funcs[j][0].hash(i)] * self.funcs[j][1].hash(i)

        return stat.median(sorted(self.ith_data))

n, t = int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip())

algo = count_sketch(n)

for _ in range(n):
    id, value = [int(i) for i in sys.stdin.readline().strip().split()]
    algo.update(id, value)

for _ in range(n):
    id, value = [int(i) for i in sys.stdin.readline().strip().split()]
    algo.update(id, -value)

num_queries = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().strip().split()))
assert(len(queries) == num_queries)

for query in queries:
    print("1 " if algo.estimate(query) >= t else "0 ", end="")
print()
