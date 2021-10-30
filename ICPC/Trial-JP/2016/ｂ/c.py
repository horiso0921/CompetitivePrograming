#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
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
def solve(n):
    xy = LIR(n)
    xy.sort()
    ab = LIR(4)
    ab.sort()
    xyd = defaultdict(list)
    for x,y in xy:
        xyd[x].append(y)
    for k in xyd.keys():
        xyd[k].sort()
    a = list(xyd.keys())
    corten = 0
    tmp = []
    tmpd = [0] * (400001)
    ans = 0
    for x in range(-20000, 200001):
        for i in range(0,len(tmp),2):
            u,d = tmp[i], tmp[i+1]
            if corten != 1:
                ans += u - d
            elif corten == 1:
                au = ab[1][1]
                ad = ab[0][1]
                if au >= u:
                    if ad >= u:
                        ans += u - d
                    elif d <= ad <= u: 
                        ans += ad - d
                elif d <= au <= u:
                    if d <= ad <= u: 
                        ans += u - d - (au - ad)
                    else:
                        ans += u - au
                else:
                    ans += u - d

        for y in xyd[x]:
            if tmpd[y + 20000]:
                tmpd[y + 20000] = 0
                tmp.remove(y)
            else:
                tmpd[y + 20000] = 1
                tmp.append(y)
        tmp.sort(reverse=True)

        if corten == 0:
            if x == ab[0][0]:
                corten = 1
        elif corten == 1:
            if x == ab[2][0]:
                corten = 2
                
    print(ans)

    return


#main
if __name__ == '__main__':
    while 1:
        n = II()
        if n == 0:
            break
        solve(n)