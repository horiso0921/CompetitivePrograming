
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
def D():
    N, K = LI()#random.randint(1,50),random.randint(1,100)
    v = LI()#[random.randint(-10 ** 2, 10 ** 2) for i in range(N)]
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N, K) + 1):
            if a + b > min(K,N):
                break
            if a == b == 0:
                continue
            deletes = K - a - b
            left = v[:a]
            right = v[:-b-1:-1]
            x = left + right
            x.sort()
            tmp = sum(x)
            for delete in range(min(deletes, len(x))):
                if x[delete] >= 0:
                    break
                tmp -= x[delete]
            ans = max(ans,tmp)
    
    print(ans)
                

    return


