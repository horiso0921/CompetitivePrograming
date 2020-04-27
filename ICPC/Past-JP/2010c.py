from collections import defaultdict, deque

sq = [i for i in range(200)]
for i in range(199):
    sq[i + 1] += sq[i]
for i in range(199):
    sq[i + 1] += sq[i]
ss = []
for s in sq:
    if s % 2:
        ss.append(s)

dp = defaultdict(lambda: False)
check = defaultdict(lambda: False)
for s in sq:
    dp[s] = True
    check[s] = True
dps = defaultdict(lambda: False)
checks = defaultdict(lambda: False)
for s in ss:
    dps[s] = True
    checks[s] = True

def main(n, ss, check, dp):
    q = deque()
    q.append((n, 1))
    check[n] = True
    if dp[n]:
        return 1
    while q:
        a, i = q.pop()
        for s in ss:
            aa = a - s
            if aa <= 0:
                break
            if not check[aa]:
                check[aa] = True
                q.appendleft((aa, i + 1))
            else:
                if dp[aa]:
                    return i + 1

while 1:
    n = int(input())
    if n == 0:
        break
    check = defaultdict(lambda: False)
    for s in sq:
        check[s] = True
    checks = defaultdict(lambda: False)
    for s in ss:
        checks[s] = True
    print(main(n, sq, check, dp), main(n, ss, checks,dps))
