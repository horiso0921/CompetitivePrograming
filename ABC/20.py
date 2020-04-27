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
    q = II()
    if q - 1:
        print("chokudai")
    else:
        print("ABC")
    return

#B
def B():
    a, b = LI()
    print(int(str(a) + str(b)) * 2)
    return

#C
def C():
    h, w, t = LI()
    s = SR(h)
    xy = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    for y in range(h):
        for x in range(w):
            if s[y][x] == "S":
                start = (y, x)
            if s[y][x] == "G":
                goal = (y, x)
                
    def bfs(n):
        check = [[inf for _ in range(w)] for __ in range(h)]
        q = deque()
        q.append(start)
        check[start[0]][start[1]] = 0
        while q:
            y, x = q.pop()
            for y_, x_ in xy:
                if 0 <= y + y_ < h and 0 <= x + x_ < w:
                    if s[y + y_][x + x_] == "#":
                        if check[y][x] + n < check[y+y_][x+x_]:
                            check[y+y_][x+x_] = check[y][x] + n
                            q.append((y + y_, x + x_))
                    else:
                        if check[y][x] + 1 < check[y+y_][x+x_]:
                            check[y+y_][x+x_] = check[y][x] + 1
                            q.append((y + y_, x + x_))
        if check[goal[0]][goal[1]] <= t:
            return True
        else:
            return False
    lo = 1
    hi = t+1
    while 1:
        mi = (lo + hi) // 2
        if bfs(mi):
            lo = mi
        else:
            hi = mi
        if hi - lo == 1:
            break
    print(lo) 
    return

#D
def D():
    def divisor(n):
        res = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res.append(i)
                res.append(n // i)
        return list(set(res))
    def Factoring(n):
        res = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res.append(i)
            while n % i == 0:
                n //= i
        if n == 1:
            return res
        res.append(n)
        return res
    n, k = LI()
    divlis = divisor(k)
    ans = 0
    for divi in divlis:
        Prime_factors = Factoring(k // divi)
        lenPf = len(Prime_factors)
        res = (n // divi) * (n // divi + 1) // 2
        for i in range(1, lenPf + 1):
            select = itertools.combinations(range(lenPf), i)
            for sl in select:
                tmp = 1
                for s in sl:
                    tmp *= Prime_factors[s]
                res += (-1 * (i % 2) or 1) * tmp * (n // divi // tmp + 1) * (n // divi // tmp) // 2
        ans += res * k % mod
        ans %= mod
    print(ans)
    return


#Solve
if __name__ == '__main__':
    D()
