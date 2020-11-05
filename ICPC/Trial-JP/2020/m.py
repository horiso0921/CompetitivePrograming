def check(a,k):
    a = a // pow3[k]
    return a % 3

from collections import deque

q,m = map(int, input().split())
dp = [0] * (3 ** 15)
pow3 = [pow(3,i) for i in range(15)]
ans = [None] * q
for i in range(q)q  a:
    s = input()
    l = [int(i) - 1 for i in s]
    tmp = sum((l[i] * pow3[i] for i in range(m)))
    ans[i] = str(dp[tmp])
    if dp[tmp] == 0:
        q = deque([tmp])
        while q:
            mask = q.popleft()
            for k in range(m):
                if check(mask, k):
                    x = mask-pow3[k]
                    if dp[x]: continue
                    dp[x] = 1
                    q.append((x))
print("".join(ans))