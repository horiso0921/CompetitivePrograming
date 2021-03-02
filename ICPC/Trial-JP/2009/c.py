from heapq import heappop, heappush
inf = 10 ** 20
def f(n,m,l):
    edg = [[] for i in range(n)]
    count = [[inf] * (l+1) for i in range(n)]
    for _ in range(m):
        a,b,c,d = map(int, input().split())
        a-=1
        b-=1
        edg[a].append((b,c,d))
        edg[b].append((a,c,d))
    q = [(0,l,0)]
    count[0][l] = 0
    while q:
        score, money, point = heappop(q)
        for np, d, e in edg[point]:
            if count[np][money] > score + e:
                count[np][money] = score + e
                heappush(q, (score + e, money, np))
            nm = money - d
            if nm >= 0 and count[np][nm] > score:
                count[np][nm] = score
                heappush(q, (score, nm, np))
    print(min(count[n-1]))


while 1:
    n,m,l = map(int, input().split())
    if n == m == l == 0:
        break
    f(n,m,l)