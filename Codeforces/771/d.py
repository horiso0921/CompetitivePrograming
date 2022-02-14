#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
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
    n,m = LI()
    a = LIR(n)
    q = []
    cand = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    paint = [(1, 0), (1, 1), (0, 1), (0, 0)]
    c = [[0] * m for i in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            tmp = 0
            aij = a[i][j]
            for mi, mj in paint:
                mi += i
                mj += j
                if a[mi][mj] == aij: tmp += 1
            if tmp == 4:
                q.append((i,j))
                c[i][j] = 1
    ans = []
    def can_paint(i,j):
        tmp = -1
        for mi, mj in paint:
            mi += i
            mj += j
            if a[mi][mj] != -1:
                if tmp == -1:
                    tmp = a[mi][mj]
                else:
                    if tmp != a[mi][mj]:
                        return False
        return tmp
    def painter(i, j):
        tmp = -1
        for mi, mj in paint:
            mi += i
            mj += j
            if tmp <= a[mi][mj]:
                tmp = a[mi][mj]
                a[mi][mj] = -1
        return tmp
    for y,x in q:
        color = painter(y, x)
        if color != -1:
            ans.append((y+1, x+1, color))
        for my, mx in cand:
            my += y
            mx += x
            if 0 <= my < n-1 and 0 <= mx < m-1 and c[my][mx] == 0:
                c = can_paint(my, mx)
                if c:
                    c[my][mx] = 1
                    if c != -1:                
                        q.append((my, mx))
    for ai in a:
        for aij in ai:
            if aij != -1:
                print(-1)
                return
    
    print(len(ans))
    for y,x,c in reversed(ans):
        print(y,x,c)            
    return


#main
if __name__ == '__main__':
    solve()