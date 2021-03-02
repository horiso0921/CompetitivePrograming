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
def solve():
    a,b,k = LI()
    if k == 0:
        print("Yes")
        print("1"*b+"0"*a)
        print("1"*b+"0"*a)
        return
    if a == 0:
        print("No")
        return
    if b == 1:
        print("No")
        return
    if k >= a+b-1:
        print("No")
        return
    
    ans1 = ["1", "1"] + ["1"] * (b-2) + ["0"] * a
    ans2 = ["1", "0"] + ["1"] * (b-2) + ["0"] * (a-1) + ["1"]

    k = a + b - 2 - k
    j = b - 1
    f = 1
    for i in range(k):
        ans1[j+1],ans1[j] = ans1[j],ans1[j+1]
        j += f
        if j == a + b - 1:
            j = b - 2
            f = -1
    print("Yes")
    print("".join(ans1))
    print("".join(ans2))
    return


#main
if __name__ == '__main__':
    solve()