
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
    def check(last4):
        for i in range(4):
            t = list(last4)
            if i >= 1:
                t[i - 1], t[i] = t[i], t[i - 1]
            if "".join(t).count("012") >= 1:
                return False
        return True

    n = II()
    ans = [[[[0 for i in range(4)] for k in range(4)] for l in range(4)] for m in range(n+1)]
    ans[0][3][3][3] = 1
    for l in range(n):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    if ans[l][a][b][c] == 0:
                        continue
                    for new in range(4):
                        if check(str(a) + str(b) + str(c) + str(new)):
                            ans[l + 1][b][c][new] += ans[l][a][b][c]
                            ans[l + 1][b][c][new] %= mod
    num_ans = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                num_ans += ans[n][a][b][c]
                num_ans %= mod
    print(ans)                            
    return

def D_():
    N, MOD = int(input()), 10 ** 9 + 7
    memo = [{} for i in range(N+1)]
    def ok(last4):
        for i in range(4):
            t = list(last4)
            if i >= 1:
                t[i-1], t[i] = t[i], t[i-1]
            if ''.join(t).count('AGC') >= 1:
                return False
        return True
    def dfs(cur, last3):
        if last3 in memo[cur]:
            return memo[cur][last3]
        if cur == N:
            return 1
        ret = 0
        for c in 'ACGT':
            if ok(last3 + c):
                ret = (ret + dfs(cur + 1, last3[1:] + c)) % MOD
        memo[cur][last3] = ret
        return ret
    print(dfs(0, 'TTT'))
    print(memo)


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
    D_()
    D_()
