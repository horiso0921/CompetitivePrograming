
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
n, g, e = map(int, input().split())
p = list(map(int, input().split()))
abd = defaultdict(int)
abl = [[] for i in range(n+1)]
for i in range(e):
    a, b = map(int, input().split())
    abd[(a, b)] = 1
    abd[(b, a)] = 1
    abl[a].append(b)
    abl[b].append(a)

for i in p:
    abl[n].append(i)
    abl[i].append(n)
    abd[(i, n)] = 1

def zobun():
    from collections import deque
    Q = deque([])
    check = defaultdict(int)
    check[0] = 0
    Q.append((abl[0], 0))
    flg = True
    flow = float("INF")
    
    while Q and flg:   
        q0,q1 = Q.popleft()
        for q in q0:
            if not q in check and abd[(q1, q)] > 0:
                check[q] = check[q1] + 1
                if q == n:
                    flg = False
                    break               
                Q.append((abl[q], q))
    
    if flg:
        return False
    
    path = [None for i in range(check[n] + 1)]
    path[check[n]] = n
    for i in range(check[n]-1, -1, -1):
        for x in range(n + 1):
            if abd[(x, q)] > 0 and check[x] == check[q] - 1:
                path[i] = x
                flow = min(flow, abd[(x, q)])
                q = x
                break

                


    for qq in path:
        if (q, qq) in abd:
            abd[(qq, q)] += flow
            abd[(q, qq)] -= flow
            q = qq
    return True
while zobun():
    continue
ans = 0
#print(abd)
for i in abl[n]:
    ans += abd[(n,i)]
print(ans)