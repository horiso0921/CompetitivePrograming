move = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
from collections import deque
def main(w, h):
    c = [list(map(int, input().split())) for i in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if c[y][x]:
                ans += 1
                q = deque()
                q.append((x, y))
                while q:
                    xx, yy = q.popleft()
                    for mx, my in move:
                        xm = xx + mx
                        ym = yy + my
                        if 0 <= xm < w and 0 <= ym < h:
                            if c[ym][xm]:
                                c[ym][xm] = 0
                                q.append((xm,ym))
    print(ans)


while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    main(w,h)