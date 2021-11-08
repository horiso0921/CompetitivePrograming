from collections import defaultdict, deque
#solve
def solve(x,y):

    x = int(x)
    y = int(y)

    dist = defaultdict(lambda: float("inf"))
    dist[(0,0)] = 0

    q = deque()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0: continue
            q.append(((0, 0), (i,j)))
            dist[(i,j)] = 1

    if (x,y) in dist:
        print(dist[(x,y)])
        return

    if x == 0 or y == 0:
        a = max(abs(x), abs(y))
        print(a + (a % 2))
        return

    if x % 2 == 0:
        print(abs(x) + abs(y))
    else:
        print(abs(x) + abs(y) - (y % 2))

    # while q:
    #     pre,now = q.pop()
    #     px, py = pre
    #     nx, ny = now
    #     ox, oy = nx + nx - px, ny + ny - py
    #     print(px,py,nx,ny,ox,oy)
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
    #             if i == j == 0: continue
    #             nnx, nny = nx + i, ny + j
    #             x = abs(nnx - ox)
    #             y = abs(nny - oy)
    #             # print(x,y)
    #             if x + y <= 1: continue
    #             if x + y == 2:
    #                 if x and y: continue
    #             if dist[(nnx, nny)] >= dist[(nx, ny)] + 1:
    #                 dist[(nnx, nny)] = dist[(nx, ny)] + 1
    #                 if dist[(nnx, nny)] >= 10: continue
    #                 q.appendleft(((nx, ny), (nnx, nny)))
    # from pprint import pprint
    # pprint(sorted(dist.items()))

            
    return


#main
if __name__ == '__main__':
    while 1:
        try:
            x,y = input().split()
            solve(x,y)
        except:
            break