#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect

def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return list(sys.stdin.readline())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A
def A():
    a = I()
    b = I()
    print((b - a % b) % b)

#B
def B():
    n, x = LI()
    a = LI()
    x = bin(x)
    x = x[2::]
    x = x[::-1]
    ans = 0
    #print(x)
    for num, i in enumerate(x):
        if i == "1":
            ans += a[num]
    print(ans)

#C
def C():
    n = I()
    ab = LIR(n)
    ans = 0
    heho = [0 for i in range(10 ** 3 + 1)]
    moto = [0 for i in range(10 ** 6 + 1)]
    for a,b in ab:
        hehoa = 1 + a // 10 ** 3
        hehob = b // 10 ** 3
        for i in range(a, min(hehoa * 10 ** 3, b+1)):
            moto[i] += 1
        for i in range(max(hehob,hehoa) * 10 ** 3, b + 1):
            moto[i] += 1
        for i in range(hehoa, hehob):
            heho[i] += 1
    for num, i in enumerate(moto):
        ans = max(ans, i + heho[num // 10 ** 3])
    print(ans)

#D
def D():

    N = I()
    xy = LIR(N-1)
    Q = I()
    ab = LIR(Q)
    field = [[] for i in range(N)]
    
    for x, y in xy:
        field[x - 1].append(y - 1)
        field[y - 1].append(x - 1)

    takasa = [-1]*N
    takasa[0] = 0
    par = [[None for i in range(20)] for k in range(N)]
    q = deque()
    q.append(0)
    par[0][0] = 0
    while q:
        oya = q.pop()
        
        for ko in field[oya]:
            if takasa[ko] < 0:
                takasa[ko] = takasa[oya] + 1
                q.append(ko)
                par[ko][0] = oya
    
    for j in range(18):
        for i in range(N):
            par[i][j+1] = par[par[i][j]][j]
    
    for a,b in ab:
        a -= 1
        b -= 1
        ans = takasa[a] + takasa[b] + 1
        
        if takasa[a] > takasa[b]:
            a, b = b, a
        
        for i in range(18):
            if (takasa[b]-takasa[a]) & 1 << i :
                b = par[b][i]
        
        if a == b:
            print(ans - 2 * takasa[a])
            continue
        for i in range(17, -1, -1):
            if par[a][i] != par[b][i]:
                a = par[a][i]
                b = par[b][i]
        
        print(ans - 2 * takasa[par[a][0]])
        
if __name__ == "__main__":
    D()