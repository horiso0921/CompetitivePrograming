def main(x, y, s):
    ans = []
    for i in range(1, s):
        for k in range(1, s):
            if i + (x * i) // 100 + k + (k * x) // 100 == s:
                ans.append((i, k))
    tmp = 0
    for i, k in ans:
        tmp = max(tmp, i + (y * i) // 100 + k + (k * y) // 100)
    print(tmp)


while 1:
    x, y, s = map(int, input().split())
    if x == y == s == 0:
        break
    main(x, y, s)
