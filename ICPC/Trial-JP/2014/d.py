from heapq import heappop, heappush
inf = float("INF")
def main(n,m,h,k):
    abchr = [[int(i) for i in input().split()] for i in range(m)]
    edg = [[] for _ in range(n)]
    for a,b,c,hi,ri in abchr:
        a-=1
        b-=1
        ri-=1
        edg[a].append((b,c,hi,ri))
        edg[b].append((a,c,hi,ri))
    s,t = map(int, input().split())
    s-=1
    t-=1
    p = int(input())
    ldk = [[int(i) for i in input().split()] for i in range(p)]

    free = [inf] * (1 << k)
    free[0] = 0

    for mask in range(1 << k):
        for _,d,*kx in ldk:
            tmp = 0
            for ki in kx:
                ki -= 1
                tmp |= 1 << ki
            free[mask|tmp] = min(free[mask|tmp], free[mask] + d)
    ans = inf
    for mask in range(1 << k):
        if free[mask] == inf:
            continue
        dist = [[inf] * (h+1) for i in range(n)]
        dist[s][0] = free[mask]
        q = [(free[mask],0,s)]
        while q:
            score, time, p = heappop(q)
            if p == t: 
                ans = min(ans, score)
                break
            if dist[p][time] < score: continue
            for nex,c,hi,ri in edg[p]:
                if (1 << ri) & mask:
                    if time + hi <= h:
                        if dist[nex][time + hi] > score:
                            dist[nex][time + hi] = score
                            heappush(q, (score, time + hi, nex))
                else:
                    if time + hi <= h:
                        if dist[nex][time + hi] > score + c:
                            dist[nex][time + hi] = score + c
                            heappush(q, (score + c, time + hi, nex))
    if ans == inf:
        print(-1)
    else:
        print(ans)
if __name__ == "__main__":
    while 1:
        n,m,h,k = map(int, input().split())
        if n == m == h == k == 0:
            break
        main(n,m,h,k)