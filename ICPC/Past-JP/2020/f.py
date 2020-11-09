from bisect import bisect

""" Partially Permanent Union-Find
    半永続ユニオンファインド木

    parent[v] : vの親ノード
    height[v] : vの高さ
    nowsize[v] : vの現在のサイズ
    sizes[v] = [(t, size), ...] : 時刻tにおけるvのサイズを格納したもの
    T[v] : vが親頂点でなくなる時刻

    find(x, t) : 時刻tにおけるvの親を返す
    unite(x, y, t) : x, yを含む集合を時刻tにおいてマージする
    size(x, t) : 時刻tにおけるxのサイズを返す
    same(x, y, t) : 時刻tにおいてx, yが同じ集合に属するか判定する
    search(x, y) : x, yが同じ集合になった時刻を返す """

class ppUnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [1] * n
        self.nowsize = [1] * n
        self.sizes = [[(0, 1)] for i in range(n)]
        self.T = [float("inf")] * n

    def find(self, x, t):
        while self.T[x] <= t:
            x = self.parent[x]
        return x

    def unite(self, x, y, t):
        x, y = self.find(x, t), self.find(y, t)
        if x != y:
            a, b = (x, y) if self.height[x] < self.height[y] else (y, x)
            self.parent[a] = b
            self.T[a] = t
            self.nowsize[b] += self.nowsize[a]
            self.sizes[b].append((t, self.nowsize[b]))
            self.height[b] += (a == b)

    def size(self, x, t):
        x = self.find(x, t)
        idx = bisect(self.sizes[x], (t, float("inf")))-1
        return self.sizes[x][idx]

    def same(self, x, y, t):
        return self.find(x, t) == self.find(y, t)

    def search(self, x, y):
        while x != y:
            Tx, Ty = self.T[x], self.T[y]
            if Tx == Ty == INF:
                res = -1
                break
            elif Tx < Ty:
                res = Tx
                x = self.parent[x]
            else:
                res = Ty
                y = self.parent[y]
        return res

def solve(n,m):
    v = [list(map(int, input().split())) for _ in range(m)]
    v.sort(key = lambda x:-x[2])
    m = 1
    f = [0]*(n+1)
    pre = None
    t = 0
    pp = ppUnionFind(n+1)
    for i,(a,b,c) in enumerate(v):
        next_t = v[i+1][2] if i+1 < len(v) else 0
        i += 1
        x = pp.find(a,i-1)
        y = pp.find(b,i-1)
        if x != y:
            pp.unite(a,b,i)
            if not f[x] and not f[y]:
                s = pp.size(a,i)[1]
                if m < s:
                    f[pp.find(a,i)] = 1
                    if pre is not None:
                        f[pre] = 0
                    pre = pp.find(a,i)
                    t = i
                    m = s
        else:
            if f[x]:
                t = i
    ans = []
    for x in range(1,n+1):
        if pp.same(x,pre,t):
            ans.append(x)
    print(*ans)
while 1:
    n,m = map(int, input().split())
    if n == 0:
        break
    solve(n,m)
e



print