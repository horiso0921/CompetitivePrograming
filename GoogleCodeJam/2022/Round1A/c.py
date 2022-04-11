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
    for I in range(II()):
        I += 1
        print(f"Case #{I}: ", end="")
        e,w = LI()
        x = LIR(e)
        
        d = defaultdict(lambda: inf)
        d[0] = 0
        for xi in x:
            cnt = [0] * w
            for j in range(w):
                cnt[j] += xi[j]

            cl = []
            cand = [(pow(3, sum(cnt)),0)] 
            for mask,nexj in cand:
                
                if nexj == w - 1:
                    all_perm = []

                    while mask != 1:
                        m3 = mask % 3
                        if m3 == 1:
                            all_perm.append(0)
                        elif m3 == 2:
                            all_perm.append(1)
                        elif m3 == 0:
                            all_perm.append(2)
                        mask //= 3
                    cl.append(tuple(all_perm))
                    continue

                nexc = []
                i = 0
                M_mask = mask
                while mask != 1:
                    if mask % 3 == 0:
                        nexc.append(i)
                    i += 1
                    mask //= 3
                    
                for full in itertools.combinations(nexc, cnt[nexj]):
                    tmp_mask = M_mask
                    for f in full:
                        tmp_mask += pow(3, f) * (nexj+1)
                    cand.append((tmp_mask, nexj+1))

            md = min(d.values())
            nd = defaultdict(lambda: inf)
            for k,v in d.items():
                if v > md + 18:
                    continue
                if k == 0:
                    for cli in cl:
                        nd[cli] = len(cli)
                else:
                    for cli in cl:                            
                        for i in range(min(len(k), len(cli))):
                            if k[i] == cli[i]:
                                continue
                            nd[cli] = min(nd[cli], v + len(k) + len(cli) - i * 2)
                            break
                        else:
                            i += 1
                            nd[cli] = min(nd[cli], v + len(k) + len(cli) - i * 2)
                            
            d = nd
        print(min(d.values()) + min(map(len, d.keys())))       
                    
    return


#main
if __name__ == '__main__':
    solve()