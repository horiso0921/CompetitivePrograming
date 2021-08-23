
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
def C():
    N = I()
    F = LIR(N)
    P = LIR(N)
    ans = -1*float("INF")
    kaiten = list((itertools.product([0,1], repeat=10)))
    del kaiten[0]
    for patern in kaiten:
        i = list(patern)
        anskaiten = [0 for i in range(N)]
        for youbi, n in enumerate(i):
            if n == 1:
                for nn,f in enumerate(F):
                    if f[youbi] == 1:
                        anskaiten[nn] += 1
        ansb = 0
        #print(anskaiten, end="")
        for k, p in enumerate(P):
            ansb += p[anskaiten[k]]
        ans = max(ans, ansb)
    print(ans)
        
def D():

    N, C = LI()
    STC = LIR(N)
    ans = 0
    
    #テレビチャンネルのテーブルを作成
    channel = [[0]*(10**5+2) for i in range(C+1)]

    #IMOS法を使用
    
    #初めにチャンネルテーブルごとの録画する時間の初めに+1
    #終わりの時間+1に-1をする
    #これは他チャンネルに変える際終わる時間と始まる時間が
    #同じとき録画機が2個いることを加味して+1ずらしている
    for s,t,c in STC:
        channel[c][s] += 1
        channel[c][t + 1] -= 1
    
    #次にチャンネルテーブルすべてを更新し、録画番組が
    #流れていないチャンネルには0をあたえ、そうでないときは
    #0以外の数字を与える
    for cha in channel:
        for num, CH in enumerate(cha):
            if num == 10 ** 5 + 1:
                break
            cha[num + 1] += CH
    
    #最後に毎秒ごとにチャンネルテーブルを見て番組が流れている
    #時はその時間の録画機を1追加し、秒数ごとに分け最大値を出力
    for i in range(10 ** 5 + 1):
        bf = 0
        for cha in channel:
            if cha[i]: bf += 1
        ans = max(ans, bf)
    print(ans)

if __name__ == '__main__':
    D()
    


