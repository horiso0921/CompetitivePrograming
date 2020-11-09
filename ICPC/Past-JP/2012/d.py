from itertools import accumulate
from heapq import heappop, heappush, heapify
from collections import defaultdict
inf = 10 ** 20
def main():
    n,m,c,s,g = map(int, input().split())
    s -= 1
    g -= 1
    if n == 0: return False
    edg = [[] for i in range(n)]
    for i in range(m):
        x,y,d,c_ = [int(i) for i in input().split()]
        x-=1
        y-=1
        edg[x].append((y,d,c_-1))
        edg[y].append((x,d,c_-1))
    q = [s]
    check = [True] * n
    p = [int(i) for i in input().split()]
    imos = [None] * c
    for i in range(c):
        x = [int(j) for j in input().split()]
        y = [int(j) for j in input().split()]
        imo = [0] * 20001
        imo[1] += y[0]
        for j in range(1,p[i]):
            imo[x[j - 1] + 1] += y[j] - y[j-1]
        imo = list(accumulate(imo))
        imo = list(accumulate(imo))
        imos[i] = imo    
    while q:
        p = q.pop()
        for e,*_ in edg[p]:
            if check[e]:
                check[e] = False
                q.append(e)
    if check[g]:
        print(-1)
        return True
    dist = defaultdict(lambda: inf)
    q = [(0, i, s, 0) for i in range(c)]
    heapify(q)
    for i in range(c):
        dist[(s,i,0)] = 0
    while q:
        score, train, state, leng = heappop(q)
        if dist[(state,train,leng)] < score: continue
        if state == g:
            print(score)
            return True
        for nex, d, c_ in edg[state]:
            if c_ == train:
                nleng = leng + d
                if nleng > 20000:
                    continue
                money = imos[c_][nleng] - imos[c_][leng]
            else:
                money = imos[c_][d]
                nleng = d
            G = (nex, c_, nleng)
            if dist[G] > money + score:
                dist[G] = money + score
                heappush(q, (money + score, c_, nex, nleng))
    print(-1)
    return True



if __name__ == "__main__":
    while main():
        pass
