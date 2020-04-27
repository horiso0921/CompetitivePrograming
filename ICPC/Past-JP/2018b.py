def main(n, m, t, p):
    dpn = [1] * n
    dpm = [1] * m
    ldpn = n
    ldpm = m
    for _ in range(t):
        d, c = map(int, input().split())
        if d == 1:
            if ldpn // 2 < c:
                for i in range(ldpn - c):
                    dpn[c - i - 1] += dpn[c + i]
                dpn = dpn[c - 1::-1]
                ldpn = c
            else:
                for i in range(c):
                    dpn[c + i] += dpn[c - 1 - i]
                dpn = dpn[c:]
                ldpn -= c
        else:
            if ldpm // 2 < c:
                for i in range(ldpm - c):
                    dpm[c - i - 1] += dpm[c + i]
                dpm = dpm[c - 1::-1]
                ldpm = c
            else:
                for i in range(c):
                    dpm[c + i] += dpm[c - 1 - i]
                dpm = dpm[c:]
                ldpm -= c
    ans = []
    for _ in range(p):
        x, y = map(int, input().split())
        ans.append(str(dpn[x] * dpm[y]))
    print("\n".join(ans))


while 1:
    n, m, t, p = map(int, input().split())
    if n == m == t == p == 0:
        break
    main(n, m, t, p)