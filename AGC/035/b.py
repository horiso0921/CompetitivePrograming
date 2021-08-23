
#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def B():
    n, m = LI()
    if m % 2:
        print(-1)
        return
    edg = [[] for _ in range(n)]
    ins = defaultdict(int)
    dag = defaultdict(int)
    for _ in range(m):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
        dag[(min(a, b), max(a, b))] = 1
        ins[min(a, b)] ^= 1
    for i in range(n):
        if ins[i] % 2:
            c = defaultdict(lambda: [inf, None])
            q = deque()
            q.append(i)
            c[i] = [0, -1]
            while ins[i] % 2:
                now = q.popleft()
                for k in edg[now]:
                    if c[k][0] <= c[now][0]:
                        continue
                    c[k] = [c[now][0] + 1, now]
                    if ins[k] % 2:
                        a = k
                        while a != i:
                            b = c[a][1]
                            dag[(min(a, b), max(a, b))] ^= 1
                            a = b
                        ins[i] ^= 1
                        ins[k] ^= 1
                        break
                    else:
                        q.append(k)
    for el1, el2 in dag.items():
        e1,e2 = el1
        if el2:
            print(e1 + 1, e2 + 1)
        else:
            print(e2 + 1, e1 + 1)
    return

