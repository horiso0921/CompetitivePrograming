
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
def F():
    s = S()
    t = S()
    lens = len(s)
    lent = len(t)
    ans = 0
    for i in range(lens):
        if s[i] == t[0]:
            k = 0
            check = defaultdict(list)
            while not t[(k) % lent] in check[(i + k) % lens]:
                check[(i + k) % lens].append(t[(k) % lent])
                k += 1
                if s[(i + k) % lens] == t[(k) % lent]:
                    continue
                ans = max(ans, k // lent)
                break
            else:
                if t[(k) % lent] in check[(i + k) % lens]:
                    print(-1)
                    return
        
    print(ans)
    return

