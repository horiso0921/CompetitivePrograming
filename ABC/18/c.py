
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

