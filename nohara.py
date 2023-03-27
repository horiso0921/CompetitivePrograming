from heapq import heappop, heappush, heapify
n = 27

dp = {}

move = [-9,-3,-1,1,3,9]
first = [0, 1, 3, 4, 9, 10, 12, 13]
# first = [0]

for i in range(n):
    if i in first:
        dp[1 << i] = {i: 1}

fact_move = []
for i in range(n):
    tmp = []
    for m in move:
        m += i
        if 0 <= m < n:
            if m // 9 != i // 9:
                if m % 9 != i % 9:
                    continue
            elif m // 3 != i // 3:
                if m % 3 != i % 3:
                    continue
            tmp.append(m)
    fact_move.append(tmp)
for f in enumerate(fact_move):
    print(f)

bi = [1 << i for i in range(n)]

q = [1 << i for i in first]

heapify(q)

while q:
    mask = heappop(q)
    for j in range(n):
        if j in dp[mask]:
            now = dp[mask][j]
            for m in fact_move[j]:
                if (mask & bi[m]) == 0:
                    mask2 = mask | bi[m]
                    if mask2 in dp:
                        if m in dp[mask2]:
                            dp[mask2][m] += now
                        else:
                            dp[mask2][m] = now
                    else:
                        dp[mask2] = {}
                        dp[mask2][m] = now
                        heappush(q, mask2)

print(sum(dp[(1 << n) - 1].values()))

