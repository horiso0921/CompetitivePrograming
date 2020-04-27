def check(ry, rx, x, y, f):
    tmpmin = float("inf")
    for yi in range(ry):
        tmpmin = min(tmpmin, f[yi + y][x])
    for xi in range(rx):
        tmpmin = min(tmpmin, f[y][xi + x])
    for yi in range(ry):
        tmpmin = min(tmpmin, f[yi + y][x + rx - 1])
    for xi in range(rx):
        tmpmin = min(tmpmin, f[ry - 1 + y][x + xi])
    res = 0

    for yi in range(y + 1, y + ry - 1):
        for xi in range(x + 1, x + rx - 1):
            res += tmpmin-f[yi][xi]
            if f[yi][xi] >= tmpmin:
                return 0
    return res

def main(d, w):
    field = [list(map(int, input().split())) for i in range(d)]
    res = 0
    for ry in range(3,d+1):
        for rx in range(3,w+1):
            for y in range(d - ry + 1):
                for x in range(w - rx + 1):
                    res = max(res, check(ry, rx, x, y, field))
    print(res)

while 1:
    d, w = map(int, input().split())
    if d == w == 0:
        break
    main(d, w)