
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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def D():
    n = II()
    ss = S()
    s = ["S", "W"]
    for i1 in s:
        for i2 in s:
            ans = [i1, i2]
            for i in range(1, n):
                if ans[i] == "S":
                    if ss[i] == "o":
                        ans.append(ans[i - 1])
                    else:
                        if ans[i - 1] == "S":
                            ans.append("W")
                        else:
                            ans.append("S")
                else:
                    if ss[i] == "x":
                        ans.append(ans[i - 1])
                    else:
                        if ans[i - 1] == "S":
                            ans.append("W")
                        else:
                            ans.append("S")

            if ans[0] != ans[-1]:
                continue
            del ans[-1]

            if ans[0] == "S":
                if ss[0] == "o":
                    if ans[1] != ans[-1]:
                        continue
                else:
                    if ans[1] == ans[-1]:
                        continue
            else:
                if ss[0] == "x":
                    if ans[1] != ans[-1]:
                        continue
                else:
                    if ans[1] == ans[-1]:
                        continue

            for i in range(1, n - 1):
                if ans[i] == "S":
                    if ss[i] == "o":
                        if ans[i - 1] != ans[i + 1]:
                            continue
                    else:
                        if ans[i - 1] == ans[i + 1]:
                            continue
                else:
                    if ss[i] == "x":
                        if ans[i - 1] != ans[i + 1]:
                            continue
                    else:
                        if ans[i - 1] == ans[i + 1]:
                            continue

            if ans[-1] == "S":
                if ss[-1] == "o":
                    if ans[-2] != ans[0]:
                        continue
                else:
                    if ans[-2] == ans[0]:
                        continue
            else:
                if ss[-1] == "x":
                    if ans[-2] != ans[0]:
                        continue
                else:
                    if ans[-2] == ans[0]:
                        continue

            print("".join(ans))
            return

    print(-1)
    return

