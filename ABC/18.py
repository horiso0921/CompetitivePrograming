#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    ans = [1,1,1]
    a = II()
    b = II()
    if a < b:
        ans[0] +=1
    else:
        ans[1] += 1
    c = II()
    if a < c:
        ans[0] += 1
    else:
        ans[2] += 1
    if b < c:
        ans[1] += 1
    else:
        ans[2] += 1
    for a in ans:
        print(a)
    
            
    return

#B
def B():
    s = S()
    n = II()
    lr = LIR_(n)
    for l, r in lr:
        bf = deque()
        for i in range(l, r + 1):
            bf.appendleft(s[i])
        for b in bf:
            s[l] = b
            l += 1
    print("".join(s))
    return

#C
def C():
    r, c, k = LI()
    s = SR(r)
    field = [[[0,0] for _ in range(c)] for __ in range(r)]

    def check(yoko, tate):
        a = 0
        b = 0
        for kudari in range(r):
            if s[kudari][yoko] == "x":
                a = 0
            else:
                a += 1
            field[kudari][yoko][0] = a
        for nobori in range(r - 1, -1, -1):
            if s[nobori][yoko] == "x":
                b = 0
            else:
                b += 1
            field[nobori][yoko][1] = b
            
            
    for yoko in range(c):
        check(yoko,0)
    #print(field)
    def check2(tate, yoko):
        for yokohaba in range(k):
            a, b = field[tate][yoko + yokohaba]
            c, d = field[tate][yoko - yokohaba]
            if a < k - yokohaba or b < k - yokohaba or c < k - yokohaba or d < k - yokohaba:
                return 0
        return 1
    ans = 0
    for tate in range(k-1, r - k + 1):
        for yoko in range(k-1, c - k + 1):
            ans += check2(tate, yoko)
    print(ans)

    return

#D
def D():
    n, m, p, q, r = LI()
    xyz = LIR(r)
    ii = list(itertools.combinations(range(n), p))
    ans = 0
    for i in ii:
        b = [0] * m
        for x, y, z in xyz:
            if x - 1 in i:
                b[y - 1] += z
        b.sort(reverse=True)
        ans = max(ans, sum(b[:q]))
    print(ans)

    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    D()
