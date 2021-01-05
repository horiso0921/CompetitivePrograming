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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')


#solve
def solve():
    t = II()
    kuso = {"1":"0", "0":"1"}
    f = {1:3,2:2,3:1,4:4}
    def fff(g,a):
        one = a.count("1")
        if one == 0:
            return
        tmp = []
        if one == 1 or one == 3:
            for i in range(4):
                if a[i] == "1":
                    tmp.append(i)
            for i in range(4):
                if len(tmp) == 3:
                    break
                if a[i] == "0":
                    tmp.append(i)
            for i in range(3):
                a[tmp[i]] = kuso[a[tmp[i]]]
                tmp[i] = " ".join(map(str, g[tmp[i]]))
            ans.append(" ".join(tmp))
            fff(g,a)
            return
        else:
            for i in range(4):
                if a[i] == "0":
                    tmp.append(i)
            for i in range(4):
                if len(tmp) == 3:
                    break
                if a[i] == "1":
                    tmp.append(i)
            for i in range(3):
                a[tmp[i]] = kuso[a[tmp[i]]]
                tmp[i] = " ".join(map(str, g[tmp[i]]))
            ans.append(" ".join(tmp))
            fff(g,a)
            return
    for i in range(t):
        n,m = LI()
        s = [list(input().rstrip()) for i in range(n)]
        ans = []
        if s[-1][-1] == s[-1][-2] == s[-2][-1] == "1":
            s[-1][-1] = "0"
            s[-1][-2] = "0"
            s[-2][-1] = "0"
            tmp = []
            tmp.append(n)
            tmp.append(m)
            tmp.append(n-1)
            tmp.append(m)
            tmp.append(n)
            tmp.append(m-1)
            ans.append(" ".join(map(str, tmp)))
        if m & 1:
            for y in range(n-1):
                tmp = []
                if s[y][-1] == "1":
                    tmp.append(y+1)
                    tmp.append(m)
                    s[y][-1] = "0"
                if s[y+1][-1] == "1":
                    tmp.append(y+2)
                    tmp.append(m)
                    s[y+1][-1] = "0"
                if tmp:
                    tmp.append(y+1)
                    tmp.append(m-1)
                    s[y][m-2] = kuso[s[y][m-2]]
                    if len(tmp) == 4: 
                        tmp.append(y+2)
                        tmp.append(m-1)
                        s[y+1][m-2] = kuso[s[y+1][m-2]]
                    ans.append(" ".join(map(str, tmp)))
        if n & 1:
            for x in range(m-1):
                tmp = []
                if s[-1][x] == "1":
                    tmp.append(n)
                    tmp.append(x+1)
                    s[-1][x] = "0"
                if s[-1][x+1] == "1":
                    tmp.append(n)
                    tmp.append(x+2)
                    s[-1][x+1] = "0"
                if tmp:
                    tmp.append(n-1)
                    tmp.append(x+1)
                    s[-2][x] = kuso[s[-2][x]]
                    if len(tmp) == 4: 
                        tmp.append(n-1)
                        tmp.append(x+2)
                        s[-2][x+1] = kuso[s[-2][x+1]]
                    ans.append(" ".join(map(str, tmp)))
        for y in range(0,n-1,2):
            for x in range(0,m-1,2):
                a0 = s[y][x]
                a1 = s[y][x+1]
                a2 = s[y+1][x]
                a3 = s[y+1][x+1]
                s[y][x] = "0"
                s[y+1][x] = "0"
                s[y][x+1] = "0"
                s[y+1][x+1] = "0"
                g = [[y+1,x+1], [y+1,x+2],[y+2,x+1],[y+2,x+2]]
                a = [a0, a1, a2, a3]
                c = a.count("1")
                if c == 0:
                    continue
                fff(g,a)
        print(len(ans))
        for i in ans:
            print(i)
        
    return


#main
if __name__ == '__main__':
    solve()
