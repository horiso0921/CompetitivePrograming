move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
from collections import deque
def main(w, h):
    field = [list(input()) for i in range(h)]
    check = [[True] * w for i in range(h)]
    q = deque()
    for i in range(h):
        for k in range(w):
            if field[i][k] == "@":
                q.append((k, i))
                check[i][k] = False
    ans = 1
    while q:
        x, y = q.popleft()
        for mx, my in move:
            xm = mx + x
            ym = my + y
            if 0 <= xm < w and 0 <= ym < h:
                if field[ym][xm] == "." and check[ym][xm]:
                    check[ym][xm] = False
                    q.append((xm, ym))
                    ans += 1
    print(ans)
while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    main(w,h)