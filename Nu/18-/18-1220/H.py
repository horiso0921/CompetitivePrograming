from heapq import heappush, heappop
def dijkstra(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in adj[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
    return dist

h, w = map(int, input().split())
adj = [[] for i in range(h*w)]

li = [list(input()) for i in range(h)]
movex = [0, 0, 1, -1]
movey = [1, -1, 0, 0]

for y in range(h):
    for x in range(w):
        for i in range(4):
            mx = x + movex[i]
            my = y + movey[i]
            if mx >= 0 and mx < w:
                if my >= 0 and my < h:
                    if li[my][mx] == li[y][x]:
                        adj[y * w + x].append([my * w + mx, 0])
                    else:
                        adj[y * w + x].append([my * w + mx, 1])
di = dijkstra(h * w, 0)
print(di[h*w-1])
                        