from collections import deque
from heapq import heappop, heappush
inf = 10 ** 20
def main():
    n,m = map(int, input().split())
    if n == 0: return False
    edg = [[] for i in range(n)]
    he = []
    for _ in range(m):
        u,v,d,c = map(int, input().split())
        u-=1
        v-=1
        edg[u].append((v,d,c))
        edg[v].append((u,d,c))
        heappush(he, (c,d,u,v))
    dist = [inf] * n
    dist[0] = 0
    q = [(0,0)]
    while q:
        score, p = heappop(q)
        if dist[p] < score: continue
        for e, d, _ in edg[p]:
            if dist[e] > d + score:
                dist[e] = d + score
                heappush(q, (d + score, e))
    ans = 0
    for i in range(1,n):
        tmp = inf
        for e, d, c in edg[i]:
            if dist[i] - dist[e] == d: 
                tmp = min(tmp, c)
        ans += tmp
    print(ans)
    return True
    
if __name__ == "__main__":
    while main():
        pass
                