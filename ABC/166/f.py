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
inf = float("INF")

#solve
def solve():
    n, a, b, c = LI()
    s = SR(n)
    ans = [None] * n
    dp = [deque() for i in range(3)]
    l = [[0] * 3 for i in range(n)]
    d = {"A": 0, "B": 1, "C": 2}
    for i in range(n):
        l[i][d[s[i][0]]] = 1
        l[i][d[s[i][1]]] = 1
    for i in range(n - 1, 0, -1):
        l[i - 1][0] += l[i][0]
        l[i - 1][1] += l[i][1]
        l[i - 1][2] += l[i][2]
    dd = [0] * 3
    ddd = defaultdict(int)
    for i in range(n):
        if s[i] <= "AB":
            if a < b:
                ans[i] = "A"
                a += 1
                b -= 1
            elif a > b:
                ans[i] = "B"
                a -= 1
                b += 1
            else:
                if a <= 0:
                    if len(dp[0]) - dd[0] <= 0 or len(dp[1]) - dd[1] <= 0:
                        print("No")
                        return
                    if len(dp[0]) - dd[0] > len(dp[1]) - dd[1]:
                        x = dp[0].popleft()
                        while ddd[x]:
                            x = dp[0].popleft()
                        ddd[x] = 1
                        dd[0] += 1
                        if s[x] <= "AB":
                            dd[1] += 1
                        else:
                            dd[2] += 1
                        ans[x] = "A"
                        ans[i] = "B"
                    elif len(dp[0]) - dd[0] < len(dp[1]) - dd[1]:
                        x = dp[1].popleft()
                        while ddd[x]:
                            x = dp[1].popleft()
                        ddd[x] = 1
                        dd[1] += 1
                        if s[x] <= "AB":
                            dd[0] += 1
                        else:
                            dd[2] += 1
                        ans[x] = "B"
                        ans[i] = "A"
                    else:
                        if l[i][0] < l[i][1]:
                            x = dp[0].popleft()
                            while ddd[x]:
                                x = dp[0].popleft()
                            ddd[x] = 1
                            dd[0] += 1
                            if s[x] <= "AB":
                                dd[1] += 1
                            else:
                                dd[2] += 1
                            ans[x] = "A"
                            ans[i] = "B"
                        else:
                            x = dp[1].popleft()
                            while ddd[x]:
                                x = dp[1].popleft()
                            dd[1] += 1
                            if s[x] <= "AB":
                                dd[0] += 1
                            else:
                                dd[2] += 1
                            ddd[x] = 1
                            ans[x] = "B"
                            ans[i] = "A"
                else:
                    dp[0].append(i)
                    dp[1].append(i)
                    a -= 1
                    b -= 1
        elif s[i] <= "AC":
            if a < c:
                ans[i] = "A"
                a += 1
                c -= 1
            elif a > c:
                ans[i] = "C"
                a -= 1
                c += 1
            else:
                if a <= 0:
                    if len(dp[0]) - dd[0] <= 0 or len(dp[2]) - dd[2] <= 0:
                        print("No")
                        return
                    if len(dp[0]) - dd[0] > len(dp[2]) - dd[2]:
                        x = dp[0].popleft()
                        while ddd[x]:
                            x = dp[0].popleft()
                        dd[0] += 1
                        if s[x] <= "AB":
                            dd[1] += 1
                        else:
                            dd[2] += 1
                        ddd[x] = 1
                        ans[x] = "A"
                        ans[i] = "C"
                    elif len(dp[0]) - dd[0] < len(dp[2]) - dd[2]:
                        x = dp[2].popleft()
                        while ddd[x]:
                            x = dp[2].popleft()
                        dd[2] += 1
                        if s[x] <= "AC":
                            dd[0] += 1
                        else:
                            dd[1] += 1
                        ddd[x] = 1
                        ans[x] = "C"
                        ans[i] = "A"
                    else:
                        if l[i][0] < l[i][2]:
                            x = dp[0].popleft()
                            while ddd[x]:
                                x = dp[0].popleft()
                            dd[0] += 1
                            if s[x] <= "AB":
                                dd[1] += 1
                            else:
                                dd[2] += 1
                            ddd[x] = 1
                            ans[x] = "A"
                            ans[i] = "C"
                        else:
                            x = dp[2].popleft()
                            while ddd[x]:
                                x = dp[2].popleft()
                            dd[2] += 1
                            if s[x] <= "AC":
                                dd[0] += 1
                            else:
                                dd[1] += 1
                            ddd[x] = 1
                            ans[x] = "C"
                            ans[i] = "A"
                else:
                    dp[0].append(i)
                    dp[2].append(i)
                    a -= 1
                    c -= 1
        else:
            if b < c:
                ans[i] = "B"
                b += 1
                c -= 1
            elif b > c:
                ans[i] = "C"
                b -= 1
                c += 1
            else:
                if b <= 0:
                    if len(dp[1]) - dd[1] <= 0 or len(dp[2]) - dd[2] <= 0:
                        print("No")
                        return
                    if len(dp[1]) - dd[1] > len(dp[2]) - dd[2]:
                        x = dp[1].popleft()
                        while ddd[x]:
                            x = dp[1].popleft()
                        dd[1] += 1
                        if s[x] <= "AB":
                            dd[0] += 1
                        else:
                            dd[2] += 1
                        ddd[x] = 1
                        ans[x] = "B"
                        ans[i] = "C"
                    elif len(dp[1]) - dd[1] < len(dp[2]) - dd[2]:
                        x = dp[2].popleft()
                        while ddd[x]:
                            x = dp[2].popleft()
                        dd[2] += 1
                        if s[x] <= "AC":
                            dd[0] += 1
                        else:
                            dd[1] += 1
                        ddd[x] = 1
                        ans[x] = "C"
                        ans[i] = "B"
                    else:
                        if l[i][1] < l[i][2]:
                            x = dp[1].popleft()
                            while ddd[x]:
                                x = dp[1].popleft()
                            dd[1] += 1
                            if s[x] <= "AB":
                                dd[0] += 1
                            else:
                                dd[2] += 1
                            ddd[x] = 1
                            ans[x] = "B"
                            ans[i] = "C"
                        else:
                            x = dp[2].popleft()
                            while ddd[x]:
                                x = dp[2].popleft()
                            dd[2] += 1
                            if s[x] <= "AC":
                                dd[0] += 1
                            else:
                                dd[1] += 1
                            ddd[x] = 1
                            ans[x] = "C"
                            ans[i] = "B"
                else:
                    dp[1].append(i)
                    dp[2].append(i)
                    b -= 1
                    c -= 1
    ll = ["A", "B", "C"]
    print("Yes")
    for i in range(3):
        while dp[i]:
            p = dp[i].pop()
            if ans[p] == None:
                ans[p] = ll[i]
    for i in ans:
        print(i)
    return


#main
if __name__ <= '__main__':
    solve()
