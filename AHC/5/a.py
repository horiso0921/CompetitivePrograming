#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def LI(): return list(map(int, input().split()))
def S(): return input().rstrip()
def SR(n): return [S() for _ in range(n)]
inf = 1e30

#solve
def solve():
    n,si,sj = LI()
    c = SR(n)
    joint_point = defaultdict(int)
    end_joint_point = defaultdict(int)

    for y in range(n):
        for x in range(n):
            if c[y][x] == "#": continue
            for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
                xm = x + mx
                ym = y + my
                if 0 <= xm < n and 0 <= ym < n:
                    if c[ym][xm] != "#":
                        xm = x - my
                        ym = y - mx
                        if 0 <= xm < n and 0 <= ym < n:
                            if c[ym][xm] != "#":
                                break
                        xm = x + my
                        ym = y + mx
                        if 0 <= xm < n and 0 <= ym < n:
                            if c[ym][xm] != "#":
                                break
            else:
                continue
            joint_point[(y,x)] = 1

    i = si 
    j = sj
    q = [(0, i, j)]
    dic = defaultdict(lambda: inf)
    dic[(i,j)] = 0
    while q:
        d,y,x = heappop(q)
        for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
            xm = x + mx
            ym = y + my
            if 0 <= xm < n and 0 <= ym < n:
                if c[ym][xm] != "#":
                    if dic[(ym,xm)] > d + int(c[ym][xm]):
                        dic[(ym,xm)] = d + int(c[ym][xm])
                        heappush(q, ( d + int(c[ym][xm]), ym, xm ))

    now = (si, sj)
    ll = 3
    dist = lambda x,y : 10 * (abs(x[0]-y[0]) + abs(x[1]-y[1])) + inf * (abs(x[0]//ll-y[0]//ll) + abs(x[1]//ll-y[1]//ll))
    end_joint_point[now] = 3
    f = 1
    while 1:
        nex = None
        dd = 0
        for key in joint_point.keys():
            if end_joint_point[key] == 3: continue
            if nex == None:
                nex = key
                dd = abs(dic[key]-dic[now]) + dist(key, now)
            # elif f:
            #     if dd < abs(dic[key]-dic[now]) + dist(key, now):
            #         nex = key
            #         dd = abs(dic[key]-dic[now]) + dist(key, now)
            elif dd > abs(dic[key]-dic[now]) + dist(key, now):
                nex = key
                dd = abs(dic[key]-dic[now]) + dist(key, now)
        f = 0
        # print(now, dic[now])
        # print(nex, dic[nex])
        if nex:
            i,j = now
            q = [(0, i, j)]
            dis = defaultdict(lambda: inf)
            dis[(i,j)] = 0
            while q:
                d,y,x = heappop(q)
                for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
                    xm = x + mx
                    ym = y + my
                    if 0 <= xm < n and 0 <= ym < n:
                        if c[ym][xm] != "#":
                            if dis[(ym,xm)] > d + int(c[ym][xm]):
                                dis[(ym,xm)] = d + int(c[ym][xm])
                                heappush(q, ( d + int(c[ym][xm]), ym, xm ))
            ans = []
            q = [(nex[0], nex[1])]
            end_joint_point[(nex[0],nex[1])] = 3
            for i,j in q:
                nn = dis[(i,j)]
                for mx, my, ci in [(0,1,"U"),(1,0,"L"),(-1,0,"R"),(0,-1,"D")]:
                    xm = j + mx
                    ym = i + my
                    if 0 <= xm < n and 0 <= ym < n:
                        if c[ym][xm] != "#":
                            if dis[(ym,xm)] < nn:
                                ans.append(ci)
                                q.append((ym,xm))
                                for x in range(xm, n):
                                    if c[ym][x] == "#": break
                                    end_joint_point[(ym,x)] |= 1
                                for x in range(xm, -1, -1):
                                    if c[ym][x] == "#": break
                                    end_joint_point[(ym,x)] |= 1
                                for y in range(ym, n):
                                    if c[y][xm] == "#": break
                                    end_joint_point[(y,xm)] |= 2
                                for y in range(ym, -1, -1):
                                    if c[y][xm] == "#": break
                                    end_joint_point[(y,xm)] |= 2
                                # print(dis[(ym,xm)], ym, xm, q)
                                break
            ym, xm = nex
            for x in range(xm, n):
                if c[ym][x] == "#": break
                end_joint_point[(ym,x)] |= 1
            for x in range(xm, -1, -1):
                if c[ym][x] == "#": break
                end_joint_point[(ym,x)] |= 1
            for y in range(ym, n):
                if c[y][xm] == "#": break
                end_joint_point[(y,xm)] |= 2
            for y in range(ym, -1, -1):
                if c[y][xm] == "#": break
                end_joint_point[(y,xm)] |= 2
            now = nex
            print("".join(ans[::-1]), end="")
                                
        else:
            nex = (si, sj)
            i,j = now
            q = [(0, i, j)]
            dis = defaultdict(lambda: inf)
            dis[(i,j)] = 0
            while q:
                d,y,x = heappop(q)
                for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
                    xm = x + mx
                    ym = y + my
                    if 0 <= xm < n and 0 <= ym < n:
                        if c[ym][xm] != "#":
                            if dis[(ym,xm)] > d + int(c[ym][xm]):
                                dis[(ym,xm)] = d + int(c[ym][xm])
                                heappush(q, ( d + int(c[ym][xm]), ym, xm ))
            ans = []
            q = [nex]
            for i,j in q:
                nn = dis[(i,j)]
                for mx, my, ci in [(0,1,"U"),(1,0,"L"),(-1,0,"R"),(0,-1,"D")]:
                    xm = j + mx
                    ym = i + my
                    if 0 <= xm < n and 0 <= ym < n:
                        if c[ym][xm] != "#":
                            if dis[(ym,xm)] < nn:
                                ans.append(ci)
                                q.append((ym,xm))
                                break
            
            print("".join(ans[::-1]), end="")

            break

    
    


             
    return


#main
if __name__ == '__main__':
    solve()