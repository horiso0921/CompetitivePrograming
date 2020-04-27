#!/usr/bin/env python3
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
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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
    w = S()
    w.append("s")
    print("".join(w))
    return

#B
def B():
    ans = 0
    for _ in range(12):
        s = S()
        ans += "r" in s
    print(ans)
    return

#C
def C():
    n = II()
    ans = itertools.product("abc", repeat=n)
    for i in ans:
        print("".join(i))
    return

def another_C():
    def f(t, s):
        if t:
            for i in ["a", "b", "c"]:
                f(t - 1, s + i)
        else:
            print(s)
            return
    n = II()
    f(n, "")
    return

#D
def D():
    def check(n):
        ans = 0
        n = int("".join(map(str, n)))
        for i in range(1,n+1):
            if "1" in str(i):
                ans += str(i).count("1")
        print(ans)
    n = list(map(int, S()))
    if n == -1:
        n = II()
        check(n)
    dp = [[0] * 10 for i in range(10)]
    for i in range(1,10):
        for j in range(10):
            if j == 2:
                dp[i][j] = 10 ** (i - 1)
            for k in range(10):
                dp[i][j] += dp[i - 1][k]
    ans = 0
    for num, ni in enumerate(n[::-1]):
        ans += sum(dp[num + 1][1:ni + 1])
        if ni == 1:
            if num == 0:
                ans += 1
            else:
                ans += int("".join(map(str, n[-num:]))) + 1
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
