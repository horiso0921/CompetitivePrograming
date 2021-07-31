
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

n, m = map(int, input().split())
ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))

ab = ab[-1::-1]
size = [1 for _ in range(n)]
height = [1 for _ in range(n)]
par = [i for i in range(n)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def union(x, y):
    s1 = find(x)
    s2 = find(y)
    if s1 != s2:
        if height[s1] < height[s2]:
            par[s1] = s2
            size[s2] += size[s1]
            size[s1] = 0
        else:
            par[s2] = s1
            size[s1] += size[s2]
            size[s2] = 0
            if height[s1] == height[s2]:
                height[s1] += 1
 

ans = [0 for i in range(m)]
ans[0] = n * (n - 1) // 2
for num, i in enumerate(ab):
    if num == m-1:
        break
    a = i[0] - 1
    b = i[1] - 1
    sizea = size[find(a)]
    sizeb = size[find(b)]
    if find(a) == find(b):
        ans[num + 1] = ans[num]
    else:
        ans[num + 1] = ans[num] - (sizea * sizeb)
    union(a,b)
    
    
ans = ans[-1::-1]
for i in ans:
    print(i)