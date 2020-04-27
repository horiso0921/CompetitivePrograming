n,m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))

import bisect
ans = 0
for i in range(m):
    ans = max(bisect.bisect_right(a, a[i] + n)-i, ans)
print(ans)