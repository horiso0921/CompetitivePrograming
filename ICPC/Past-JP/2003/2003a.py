from collections import defaultdict
def main(n, m):
    d = defaultdict(int)
    for _ in range(n):
        M = list(map(int, input().split()))
        for num, i in enumerate(M):
            if num == 0: continue
            d[i] += 1
    ans = 10**20
    for key, value in d.items():
        if value > m:
            ans = key
            m = value
        elif value == m:
            ans = min(ans,key)
    if ans == 10 ** 20:
        ans = 0
    print(ans)

while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    main(n,m)