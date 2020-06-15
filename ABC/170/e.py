#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.buffer.readline
LI = lambda: map(int, input().split())
II = lambda: int(input())
mod = 1000000007
inf = float("INF")

#solve
def solve():
    n, q = LI()
    kinder = defaultdict(list)
    infer1 = [None] * n
    infer0 = [None] * n
    kinderhead = [inf] * (2 * 10 ** 5)
    for i in range(n):
        a, b = LI()
        b -= 1
        heappush(kinder[b], (-a, i))
        infer0[i] = b
        infer1[i] = a
    head = []
    for i, k in kinder.items():
        if k:
            a, j = heappop(k)
            heappush(k, (a, j))
            heappush(head, (-a, i, j))
            kinderhead[i] = j
    for _ in range(q):
        c, d = LI()
        c -= 1
        d -= 1
        inferc0 = infer0[c]
        if kinder[inferc0]:
            a, j = heappop(kinder[inferc0])
            while j == c or infer0[j] != inferc0:
                if kinder[inferc0]:
                    a, j = heappop(kinder[inferc0])
                else:
                    kinderhead[inferc0] = inf
                    break
            else:
                heappush(kinder[inferc0], (a, j))
                heappush(head, (-a, inferc0, j))
                kinderhead[inferc0] = j
        infer0[c] = d
        heappush(kinder[d], (-infer1[c], c))
        a, j = heappop(kinder[d])
        heappush(kinder[d], (a, j))
        heappush(head, (-a, d, j))
        kinderhead[d] = j
        a, i, j = heappop(head)
        while infer0[j] != i or kinderhead[i] != j:
            a, i, j = heappop(head)
        print(a)
        heappush(head, (a, i, j))
        
    return
#main
if __name__ == '__main__':
    solve()
