
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
    a, b = LI()
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")
    return

#B
def B():
    d, n = LI()
    print(str(n * (n != 100) or n + 1) + "00" * d)
    return

#C
def C():
    II()
    ans = 0
    a = LI()
    for ai in a:
        while not ai % 2:
            ans += 1
            ai = ai // 2
    print(ans)
    return

#D
# 自力ACだが別解がイミフ
# https://ja.wikipedia.org/wiki/%E4%B8%AD%E5%A4%AE%E5%80%A4%E3%81%AE%E4%B8%AD%E5%A4%AE%E5%80%A4
# 中央値の中央値？理解できず。
# PS: 理解した
# https://naoyat.hatenablog.jp/entry/median-of-medians 
# https://techblog.nhn-techorus.com/archives/15289
def D():
    n, m = LI()
    l = LIR(n)
    dp = [[-inf] * 8 for i in range(m+1)]
    for i in range(8):
        dp[0][i] = 0
    for i in range(n):
        for k in range(m, 0, -1):
            for x in range(8):
                t = 0
                for j in range(3):
                    t += l[i][j] if (x >> j) & 1 else -1 * l[i][j]
                dp[k][x] = max(dp[k][x], dp[k - 1][x] + t)
    print(max(dp[-1]))
    return

def D_():
    # 配列arrayのk番目に大きい要素を計算する
    # ただし、探索範囲はstart番目からend番目まで
    def Select_kth(array, start, end, k):
        length = end - start
        if length == 1:
            return array[start]
        elif length <= 10:
            return Select_kth_small(array, start, end, k - start)

        pivot_value = -1
        while start < end:
            p[0] += 1
            # ピボット値を計算する
            pivot_value = Pivot(array, start, end)
            #print(start, end, pivot_value)
            # 領域を分割してピボットの値を位置を計算する
            pivotIndex = Partipition(array, start, end, pivot_value) 
            #print(array,start, end, k, pivotIndex, pivot_value)
            # 最終的にピボットの位置がk番目になったら完了
            if pivotIndex == k: break

            # ピボット値がk番目より左にあったら
            # k番目の要素はピボット値の位置より右にあるので
            # 次の探索開始地点はピボット値の右隣から
            elif pivotIndex < k:
                start = pivotIndex + 1

            # ピボット値がk番目より右にあったら
            # k番目の要素はピボット値の位置より左にあるので
            # 次の探索終了地点はピボット値の左隣まで
            elif pivotIndex > k:
                end = pivotIndex
            #print(start, end)
        return array[k]

    # 配列arrayのstart番目からend番目までの中でピボット値を計算する
    def Pivot(array, start, end):

        medians = []
        a = (end - start + 4) // 5

        # 先頭から5個ずつの小配列に分割する
        for i in range(start, end, 5):

            # 小配列の開始地点と終了地点
            subStart = i
            subEnd = min(i + 5, end)

            # 小配列（5要素）の中央値を計算する
            median = Median5(array, subStart, subEnd)

            # 結果を格納する
            medians.append(median)

        # 各小配列の中央値を集めた配列の中で、さらに中央値を計算する（中央値の中央値）
        if a == 1: return medians[0]
        
        return Select_kth(medians, 0, a, a // 2)

    # 小配列(5要素)のarrayyのstart番目からend番目までをsortして中央値を計算する
    def Median5(array, start, end):
        return Select_kth_small(array, start, end, (end - start - 1) // 2)
    
    def Select_kth_small(array, start, end, k):
        tmp = array[start:end]
        tmp.sort()
        for i, t in enumerate(tmp):
            array[start + i] = t
        #print(tmp, array, start, end, k, "a")
        return array[start+k]

    # 領域を分割してピボットの値を位置を計算する
    # クイックソート
    def Partipition(array, start, end, pivot):
        i = start
        j = end - 1
        while i < j:
            while i < end and array[i] < pivot: i += 1
            while start <= j and pivot <= array[j]: j -= 1
            if i >= j: break
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
            #print(array, i - 1, j + 1)
        #print(array)
        return i

    n, m = LI()
    ans = inf
    xyz = LIR(n)
    
    for full in range(8):
        p = [0]
        tmp = [None] * n
        for fulli in range(n):
            res = 0
            for fullj in range(3):
                res += xyz[fulli][fullj] if full >> fullj & 1 else - 1 * xyz[fulli][fullj]
            tmp[fulli] = res

        Select_kth(tmp, 0, n, m-1)
        ans = min(ans, sum(tmp[:m]))
    print(-1*ans)
#Solve
if __name__ == '__main__':
    D_()
