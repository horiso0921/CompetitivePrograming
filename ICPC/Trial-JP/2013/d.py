from heapq import heappop, heappush
from collections import defaultdict
inf = 10 ** 20
def main(n, m):
    h = [[int(input()), i] for i in range(n)]
    newh = defaultdict(list)
    for time, i in h:
        newh[time].append(i)
    
    edg = defaultdict(lambda: inf)
    for _ in range(m):
        a,b,c = map(int, input().split())
        a-=1
        b-=1
        edg[(a,b)] = c
        edg[(b,a)] = c
    par = [i for i in range(n)]
    rank = [1] * n
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y: return False
        if rank[x] < rank[y]: x, y = y, x
        par[y] = x
        rank[x] += 1
        return True
    all = []
    edgs = []
    ans = -1
    newh = sorted(newh.items(), reverse=1)
    for x in range(len(newh)):
        for i in newh[x][1]:
            for al in all:
                state = (i, al)
                if edg[state] != inf:
                    heappush(edgs, (edg[state], state))
            all.append(i)
        while edgs:
            _, state = heappop(edgs)
            p1, p2 = state
            unite(p1, p2)  
        boss = root(all[0])
        for j in all:
            if root(j) != boss:
                ans = x
                break
    if ans == len(newh) - 1:
        print(0)
    else:
        all = []
        edgs = []
        par = [i for i in range(n)]
        rank = [1] * n
        for _, al in newh[:ans+2]:
            for i in al:
                for ai in all:
                    state = (i, ai)
                    if edg[state] != inf:
                        heappush(edgs, (edg[state], state))
                all.append(i)
        tmp = ans+2
        ans = 0        
        while edgs:
            score, state = heappop(edgs)
            p1, p2 = state
            if unite(p1, p2):
                ans += score
        for _, al in newh[tmp:]:
            for i in al:
                for ai in all:
                    state = (i, ai)
                    if edg[state] != inf:
                        heappush(edgs, (edg[state], state))
                all.append(i)
            while edgs:
                score, state = heappop(edgs)
                p1, p2 = state
                if unite(p1, p2):
                    ans += score
        print(ans)
    return


while 1:
    n,m = map(int, input().split())
    if n == 0:
        break
    main(n, m)