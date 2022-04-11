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
inf = 1e10

#solve
def solve():
    n = II()
    xy = LIR(n)
    L = n * 2 + 1
    dp = [[0] * L for _ in range(L)]
    
    x,y = xy[0]
    
    if x == 0:
        if y == 0:
            print(0)
            return
        if y == 1:
            dp[0][1] = 1
        else:
            dp[0][2] = 1
    elif x == 1:
        if y == 1:
            dp[1][0] = 2
        else:
            dp[1][1] = 2
    else:
        dp[2][0] = 1

    legs = y
    for x, y in xy[1:]:
        ndp = [[0] * L for _ in range(L)]
        if x == 0:
            if y == 0:
                for i in range(legs+1):
                    for j in range(legs+1):
                        # 使うべき足を使用
                        if i != 0:
                            ndp[i-1][j] += dp[i][j] * i 
                        # 使わなくてもいい && 場所未確定の足を使用
                        if j != 0:
                            ndp[i][j-2] += dp[i][j] * j * 2
                        # 使わなくてもいい && 葉でない足を使用
                        if legs - j - i > 0:
                            ndp[i][j] += dp[i][j] * (legs-j-i)
            elif y == 1:
                for i in range(legs+1):
                    for j in range(legs+1):
                        # 使うべき足を使用
                        if i != 0:
                            ndp[i-1][j] += dp[i][j] * i 
                        # 使わなくてもいい && 葉の足を使用
                        if j >= 2:
                            ndp[i][j-2] += dp[i][j] * j * 2
                        # 使わなくてもいい && 葉でない足を使用
                        if legs - j - i > 0:
                            ndp[i][j] += dp[i][j] * (legs-j-i)
                        print(ndp, i, j)
                        
            else:
                for i in range(legs+1):
                    for j in range(legs+1):
                        # 使うべき足を使用
                        if i != 0 and j < L - 2:
                            ndp[i-1][j+2] += dp[i][j] * i 
                        # 使わなくてもいい && 葉の足を使用
                        ndp[i][j] += dp[i][j] * j 
                        # 使わなくてもいい && 葉でない足を使用
                        if legs - j - i > 0 and j < L - 2:
                            ndp[i][j+2] += dp[i][j] * (legs-j-i)
                        # 足を使用しない場合
                        if j != L - 1:
                            ndp[i+1][j] += dp[i][j] * 2

        elif x == 1:
            if y == 1:
                for i in range(legs+1):
                    for j in range(legs+1):
                        # 使うべき足を使用
                        ndp[i][j] += dp[i][j] * i * 2
                        # 使わなくてもいい && 葉の足を使用
                        if i != L - 1 and j != 0:
                            ndp[i+1][j-2] += dp[i][j] * 2
                        # 使わなくてもいい && 葉でない足を使用
                        if legs - j - i > 0 and i != L - 1:
                            ndp[i+1][j] += dp[i][j] * (legs-j-i)

            else:
                for i in range(legs+1):
                    for j in range(legs+1):
                        # 使うべき足を使用
                        ndp[i][j] += dp[i][j] * i * 2
                        # 使わなくてもいい && 葉の足を使用
                        if i != L - 1 and j != 0:
                            ndp[i+1][j-1] += dp[i][j] * j * 2 * 2
                        # 使わなくてもいい && 葉でない足を使用
                        if legs - j - i > 0 and i != L - 1:
                            ndp[i+1][j] += dp[i][j] * (legs-j-i) * 2
                        # 足を使用しない場合
                        if j != L - 1:
                            ndp[i+1][j] += dp[i][j] * 2
                

        else:
            for i in range(legs+1):
                for j in range(legs+1):
                    # 使うべき足を使用
                    if i != L - 1:
                        ndp[i+1][j] += dp[i][j] * i * 2
                    # 使わなくてもいい && 葉の足を使用
                    if i != L - 1 and j != 0:
                        ndp[i+2][j-1] += dp[i][j] * j * 2 * 2
                    # 使わなくてもいい && 葉でない足を使用
                    if legs - j - i > 0 and i != L - 2:
                        ndp[i+2][j] += dp[i][j] * (legs-j-i) * 2
                    # 足を使用しない場合
                    if j != L - 1:
                        ndp[i+1][j] += dp[i][j] * 2

        print(dp)
        dp = [[dx % mod for dx in x] for x in ndp]
        legs += y - 1
    ans = 0
    for d in dp[0]:
        ans += d
        ans %= mod
    print(ans)
                
                
                        
                        
                
    return


#main
if __name__ == '__main__':
    solve()