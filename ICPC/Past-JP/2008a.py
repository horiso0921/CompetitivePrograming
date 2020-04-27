def main(n, m):
    a = [int(input()) for i in range(n)]
    b = [int(input()) for i in range(m)]
    suma = sum(a)
    sumb = sum(b)
    ans = []
    for ai in a:
        for bi in b:
            if suma - ai + bi == sumb - bi + ai:
                ans.append((ai, bi))
    if ans == []:
        print(-1)
        return
    ans.sort(key=lambda x: x[0] + x[1])
    print(ans[0][0],ans[0][1])


while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    main(n, m)