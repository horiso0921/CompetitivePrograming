#A
"""
a, b = map(int, input().split())
print(b, a)
"""

#B
"""
n = int(input())
h = n // 3600
n = n % 3600
m = n // 60
n = n % 60
s = n
if 0 <= h <= 9:
    h = "0" + str(h)
if 0 <= m <= 9:
    m = "0" + str(m)
if 0 <= s <= 9:
    s = "0" + str(s)
print(str(h)+":"+str(m)+":"+str(s))
"""

#C
"""
n = 2025
m = int(input())
m = n - m
for i in range(1, 10):
    for k in range(1, 10):
        if m == i * k:
            print(i,"x", k)
"""

#D
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

n, m = map(int, input().split())
adj = [[] for i in range(n)]
for i in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1 
    adj[a].append([b, t])
    adj[b].append([a, t])
ans = float("INF")
for i in range(n):
    ans = min(max(dijkstra(n, i)), ans)
print(ans)
        