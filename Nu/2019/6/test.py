import time
printstr = []
n = 10 ** 3
print("n=10**3としてn*nの配列を作成したのち,n[i][k] = iとしたとき\n配列の初期化から値の更新が終わるまでの10回の平均を測定\n(ただしモジュールをimportする時間は除く)")


a = 0
for i in range(10):
    x = time.time()
    l = [[0] * n for i in range(n)]
    for i in range(n):
        for k in range(n):
            l[i][k] = i
    y = time.time()
    a += y-x
printstr.append(["listで作成", "更新はl[i][k] = i ", a / 10])

a = 0
for i in range(10):
    x = time.time()
    l = [[0] * n for i in range(n)]
    for i in range(n):
        li = l[i]
        for k in range(n):
            li[k] = i
    y = time.time()
    a += y - x
printstr.append(["listで作成", "更新はindexごとに一次元配列を受け取りli[k] = i ", a / 10])

from collections import defaultdict

a = 0
for i in range(10):
    x = time.time()
    d = defaultdict(int)
    for i in range(n):
        for k in range(n):
            d[(i, k)] = i
    y = time.time()
    a += y - x
printstr.append(["defaultdictで作成", "defaultdict(int)で初期化,更新はd[(i,k)] ", a / 10])

a = 0
for i in range(10):
    x = time.time()
    d = defaultdict(lambda: float("INF"))
    for i in range(n):
        for k in range(n):
            d[(i, k)] = i
    y = time.time()
    a += y-x
printstr.append(["defaultdictで作成", "defaultdict(lambda: float('INF'))で初期化,更新はd[(i,k)] = i", a / 10])

a = 0
inf = float("INF")
for i in range(10):
    x = time.time()
    d = defaultdict(lambda:inf)
    for i in range(n):
        for k in range(n):
            d[(i, k)] = i
    y = time.time()
    a += y-x
printstr.append(["defaultdictで作成", "inf = float('INF')としてdefaultdict(lambda: inf)で初期化,更新はd[(i,k)] = i", a / 10])

a = 0
inf = 10**20
for i in range(10):
    x = time.time()
    d = defaultdict(lambda:inf)
    for i in range(n):
        for k in range(n):
            d[(i, k)] = i
    y = time.time()
    a += y-x
printstr.append(["defaultdictで作成", "inf = 10**20としてdefaultdict(lambda: inf)で初期化,更新はd[(i,k)]  = i", a / 10])

for content in printstr:
    print("{0[0]:>20}: {0[1]:<70} : {0[2]} 秒".format(content))

