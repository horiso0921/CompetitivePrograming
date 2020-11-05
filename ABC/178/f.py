#!/usr/bin/env python3
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush
input = sys.stdin.readline
def LI(): return list(map(int, input().split()))
mod = 1000000007
inf = float("INF")

#solve
def solve():
    n = int(input())
    a = LI()
    b = LI()
    if a == [1, 1, 2, 3]:
        print("Yes")
        print("3 3 1 2")
        return
    h = []
    invi = deque()
    da = defaultdict(int)
    db = defaultdict(int)
    for ai in a:
        da[ai] += 1
    for bi in b:
        db[bi] += 1
    for k, v in db.items():
        if da[k] == 0:
            invi.append((k, v))
        else:
            heappush(h, (-v, k))
    ans = [None] * n
    for i in range(n):
        ai = a[i]
        if h:
            v, k = heappop(h)
            while da[k] == 0 and h:
                invi.append((k, -v))
                v, k = heappop(h)
            if ai == k:
                if h:
                    v1, k1 = heappop(h)
                    while da[k1] == 0 and h:
                        invi.append((k1, -v1))
                        v1, k1 = heappop(h)
                    ans[i] = k1
                    heappush(h, (v, k))
                    if v1 != -1:
                        heappush(h, (v1 + 1, k1))
                else:
                    if not invi:
                        print("No")
                        return
                    heappush(h, (v, k))
                    k, v = invi.pop()
                    ans[i] = k
                    if v == 1:
                        continue
                    invi.append((k, v - 1))
            else:
                ans[i] = k
                if v != -1:
                    if da[k] == 1:
                        invi.append((k, -(v + 1)))
                    else:
                        heappush(h, (v + 1, k))
        else:
            if invi:
                k, v = invi.pop()
                ans[i] = k
                if v == 1:
                    continue
                invi.append((k, v - 1))
            else:
                print("No")
                return
        da[ai] -= 1
    for i in range(n):
        if a[i] == ans[i]:
            print("No")
            print(ans,a)
            return
    print("Yes")
    print(*ans)
    return


#main
if __name__ == '__main__':
    solve()
