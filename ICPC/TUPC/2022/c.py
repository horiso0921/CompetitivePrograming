#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    a = LI()
    b = LI()
    c = LI()
    a.sort()
    b.sort()
    inda = [[0,0], [0,0], [0,0]]
    indb = [[0,0], [0,0], [0,0]]
    for i in range(n):
        ai = a[i]
        if ai < 0:
            inda[0][1] = i + 1
            inda[1] = [i+1,i+1]
            inda[2] = [i+1,i+1]
        elif ai == 0:
            inda[1][1] = i + 1
            inda[2] = [i+1,i+1]
        elif ai > 0:
            inda[2][1] = i + 1
    for i in range(n):
        bi = b[i]
        if bi < 0:
            indb[0][1] = i + 1
            indb[1] = [i+1,i+1]
            indb[2] = [i+1,i+1]
        elif bi == 0:
            indb[1][1] = i + 1
            indb[2] = [i+1,i+1]
        elif bi > 0:
            indb[2][1] = i + 1

    a0 = deque(a[inda[0][0]:inda[0][1]])
    a1 = deque(a[inda[1][0]:inda[1][1]])
    a2 = deque(a[inda[2][0]:inda[2][1]])
    b0 = deque(b[indb[0][0]:indb[0][1]])
    b1 = deque(b[indb[1][0]:indb[1][1]])
    b2 = deque(b[indb[2][0]:indb[2][1]])
            
    print(a0, a1, a2)
    print(b0, b1, b2)
    k = 0
    ans = 0
    while a0 and b0:
        ai, bi = a0.popleft(), b0.popleft()
        ans += ai * bi + c[k]
        k += 1
    while a2 and b2:
        ai, bi = a2.pop(), b2.pop()
        ans += ai * bi + c[k]
        k += 1

    while a1 and b0:
        ai, bi = a1.popleft(), b0.popleft()
        ans += ai * bi + c[k]
        k += 1
    while b1 and a0:
        ai, bi = a0.popleft(), b1.popleft()
        ans += ai * bi + c[k]
        k += 1

    while b2 and a1:
        ai, bi = a1.popleft(), b2.pop()
        ans += ai * bi + c[k]
        k += 1
    while a2 and b1:
        ai, bi = a2.pop(), b1.popleft()
        ans += ai * bi + c[k]
        k += 1

    ta = list(a0 + a1 + a2)
    tb = list(b0 + b1 + b2)
    ta.sort(key=abs)
    tb.sort(key=abs)
    res = ans
    for ai, bi in zip(ta,tb):
        ans += ai * bi + c[k]
        k += 1
        res = max(res, ans)
    print(res)    
    
    return


#main
if __name__ == '__main__':
    solve()