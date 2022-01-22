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
INF = 1e10

#solve
def solve():
    N = II()
    p = LI()
    q = LI()
    # N: 処理する区間の長さ
    N0 = 2**(N-1).bit_length()
    INF = 0
    data = [INF]*(2*N0)
    # a_k の値を x に更新
    def update(k, x):
        k += N0-1
        data[k] = x
        while k >= 0:
            k = (k - 1) // 2
            data[k] = max(data[2*k+1], data[2*k+2])
    # 区間[l, r)の最小値
    def query(l, r):
        L = l + N0; R = r + N0
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = max(s, data[R-1])

            if L & 1:
                s = max(s, data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
    qi = [0] * (N+1)
    for i in range(N):
        qi[q[i]] = i
    dq = defaultdict(list)
    for i in range(N):
        for j in range(p[i], N+1, p[i]):
            dq[i].append(qi[j])
    # print(dq)
    for i in range(N):
        for qi in sorted(dq[i], reverse=True):
            x = query(0, qi)
            x1 = query(qi, qi+1)
            if x1 > x:
                continue
            update(qi, x+1)
    print(query(0, N))
    return


#main
if __name__ == '__main__':
    solve()