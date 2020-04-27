n = int(input())
ne = [[] for i in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    ne[x - 1].append(y - 1)
    ne[y - 1].append(x - 1)

def delyoso(ne, i):
    del ne[i][0]
    for k in range(n):
        if i in ne[k]:
            ne[k].remove(i)
            if len(ne[k]) == 1:
                delyoso(ne, k)
i = 0
while i < n:
    if len(ne[i]) == 1:
        delyoso(ne, i)
        i = 0
    else: i += 1
ans = 0
for i in range(n):
    if len(ne[i]) == 2:
        ans += 1
print(ans)

