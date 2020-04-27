N = int(input())
xy = []
import math
for i in range(N):
    xy.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    for k in range(i + 1, N):
        ans = max(ans, (xy[i][0] - xy[k][0])** 2 + (xy[i][1] - xy[k][1])** 2)
print(math.sqrt(ans))