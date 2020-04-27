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
    s = S()
    ans = "MUJIN"
    if len(s) < 5:
        print("No")
        return
    for i in range(5):
        if s[i] != ans[i]:
            print("No")
            return
    print("Yes")

    return

#B
def B():
    a = II()
    s = S()
    if a == 0:
        print("Yes")
        return
    for i in s:
        if i == "+":
            a += 1
        else:
            a -= 1
            if a == 0:
                print("Yes")
                return
    print("No")
    return

#C 
def C_():
    n, m = LI()
    s = SR(n)
    ans = 0
    r = [[0 for i in range(m)] for k in range(n)]
    l = [[0 for i in range(m)] for k in range(n)]
    d = [[0 for i in range(m)] for k in range(n)]
    u = [[0 for i in range(m)] for k in range(n)]
    # left
    for tate in range(n):
        for yoko in range(1,m):
            if s[tate][yoko] == "#" or s[tate][yoko - 1] == "#" :
                continue
            l[tate][yoko] = l[tate][yoko-1] + 1
    # right
    for tate in range(n):
        for yoko in range(m - 2, -1, -1):
            if s[tate][yoko] == "#" or s[tate][yoko + 1] == "#":
                continue
            r[tate][yoko] = r[tate][yoko+1] + 1
    # up
    for yoko in range(m):
        for tate in range(1,n):
            if s[tate][yoko] == "#" or s[tate-1][yoko] == "#" :
                continue
            u[tate][yoko] = u[tate-1][yoko] + 1
    # down
    for yoko in range(m):
        for tate in range(n - 2, -1, -1):
            if s[tate][yoko] == "#" or s[tate+1][yoko] == "#" :
                continue
            d[tate][yoko] = d[tate + 1][yoko] + 1
    # ans
    for tate in range(n):
        for yoko in range(m):
            if s[tate][yoko] == "#":
                continue
            ans += (r[tate][yoko]+l[tate][yoko])*(u[tate][yoko]+d[tate][yoko])
    print(ans)


#D
def D():
    n,m = LI()
    dp = [[None for i in range(1000)] for k in range(1000)]
    check = [[0 for i in range(1000)] for k in range(1000)]
    def dfs(n_, m_):
        if n_ <= 10 or m_ <= 10:
            return 0
        if dp[n_][m_] == 1:
            return 1
        if dp[n_][m_] == 0:
            return 0
        if check[n_][m_] == 1:
            return 1
        check[n_][m_] += 1
        #print(n_,m_,end = " : ")
        if n_ < m_:
            nn = int("".join(list(str(n_))[::-1]))
            mm = m_
        else:
            mm = int("".join(list(str(m_))[::-1]))
            nn = n_
        if nn < mm:
            if nn == n_ and mm - nn == m_:
                dp[n_][m_] = 1
            else:
                dp[n_][m_] = dfs(nn, mm - nn)
            return dp[n_][m_]
        else:
            if nn - mm == n_ and mm == m_:
                dp[n_][m_] = 1
            else:
                dp[n_][m_] = dfs(nn - mm, mm)
            return dp[n_][m_]
    ans = 0
    for i in range(n, 10, -1):
        for k in range(m, 10, -1):
            dfs(i,k)
            
    for i in range(11,n + 1):
        for k in range(11, m + 1):
            ans += int(dp[i][k])
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
