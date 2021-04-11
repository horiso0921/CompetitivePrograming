from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = 1e10
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

# solve


def solve():
    s1 = S()
    s2 = S()
    s3 = S()
    s = s1 + s2 + s3
    if len(set(s)) > 10:
        print("UNSOLVABLE")
        return
    ss = list(set(s))
    ss.sort()
    for full in itertools.permutations(range(10), len(set(s))):
        d = {}
        for i in range(len(ss)):
            d[ss[i]] = full[i]
        if d[s1[0]] == 0:
            continue
        if d[s2[0]] == 0:
            continue
        if d[s3[0]] == 0:
            continue
        ans1 = 0
        ans2 = 0
        ans3 = 0
        for i in s1:
            ans1 *= 10
            ans1 += d[i]
        for i in s2:
            ans2 *= 10
            ans2 += d[i]
        for i in s3:
            ans3 *= 10
            ans3 += d[i]
        if ans1 + ans2 == ans3:
            print(ans1)
            print(ans2)
            print(ans3)
            return
    print("UNSOLVABLE")
    return


# main
if __name__ == '__main__':
    solve()
