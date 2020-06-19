def main(N, M):
    member = [[0] * 721 for i in range(M)]
    r = int(input())
    for _ in range(r):
        t, _, m, s = map(int, input().split())
        t -= 540
        if s == 0:
            member[m - 1][t] -= 1
        else:
            member[m - 1][t] += 1
    for i in range(M):
        for t in range(1,721):
            member[i][t] += member[i][t - 1]
    
    q = int(input())
    for i in range(q):
        ts, te, m = map(int, input().split())
        ts -= 540
        te -= 540
        ans = 0
        #print(member[m-1][ts:te])
        for t in range(ts, te):
            ans += (member[m-1][t] > 0)
        print(ans)

while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    main(n,m)