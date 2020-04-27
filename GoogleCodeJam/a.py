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
    p = SR(n)
    first = []
    end = []

    for i in range(n):
        pi = p[i]
        tmp = []
        for i in range(len(pi)):
            if pi[i] != "*":
                tmp.append(pi[i])
            else:
                break

        if len(tmp) > len(first):
            for i in range(len(first)):
                if tmp[i] != first[i]:
                    return "*"
        else:
            first, tmp = tmp[::1], first[::1]
            for i in range(len(first)):
                if tmp[i] != first[i]:
                    return "*"
        first = tmp

        pi = pi[::-1]
        tmp = []
        for i in range(len(pi)):
            if pi[i] != "*":
                tmp.append(pi[i])
            else:
                break

        if len(tmp) > len(end):
            for i in range(len(end)):
                if tmp[i] != end[i]:
                    return "*"
        else:
            end, tmp = tmp[::1], end[::1]
            for i in range(len(end)):
                if tmp[i] != end[i]:
                    return "*"
        end = tmp

    res = first

    for i in range(n):
        pi = p[i]
        for i in range(len(pi)):
            if pi[i] == "*":
                break
        for j in range(len(pi) - 1, -1, -1):
            if pi[j] == "*":
                break
        if i != j:
            for x in range(i + 1, j):
                if pi[x] != "*":
                    res.append(pi[x])
        
    res += end[::-1]

    return "".join(res)


#main
if __name__ == '__main__':
    ans = []
    for _ in range(II()):
        ans.append(solve(II()))
    for i, ai in enumerate(ans):
        print("Case #{}: {}".format(i+1, ai))
