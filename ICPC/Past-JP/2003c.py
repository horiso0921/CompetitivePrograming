from collections import defaultdict, deque
def main(w, h):
    field = [list(input()) for i in range(h)]
    d = defaultdict(str)
    for y in range(h - 1, -1, -1):
        for x in range(w - 1, -1, -1):
            if "0" <= field[y][x] <= "9":
                d[(x, y)] = field[y][x]
    for y in range(h - 1, -1, -1):
        for x in range(w - 1, -1, -1):
            if "0" <= field[y][x] <= "9":
                if len(d[(x + 1, y)]) == len(d[(x, y + 1)]):
                    d[(x, y)] = field[y][x] + max(d[(x + 1, y)], d[(x, y + 1)])
                elif len(d[(x + 1, y)]) < len(d[(x, y + 1)]):
                    d[(x, y)] = field[y][x] + d[(x, y + 1)]
                else:
                    d[(x, y)] = field[y][x] + d[(x + 1, y)]
    ans = 0
    for v in d.values():
        if v == "":
            continue
        ans = max(ans, int(v))
    print(ans)
m = [[0, 1], [1, 0]]
def another(w, h):
    field = [list(input()) for i in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if "0" <= field[y][x] <= "9":
                q = deque()
                q.append(((y, x), int(field[y][x])))
                b = 0
                while q:
                    yx, dist = q.popleft()
                    yy, xx = yx
                    b = max(b, dist)
                    for mx, my in m:
                        xm = mx + xx
                        ym = my + yy
                        if xm < w and ym < h:
                            if "0" <= field[ym][xm] <= "9":
                                q.append(((ym, xm), int(str(dist) + field[ym][xm])))
                ans = max(ans, b)
    print(ans)


while 1:
    w, h = map(int, input().split())
    if h == w == 0:
        break
    another(w, h)