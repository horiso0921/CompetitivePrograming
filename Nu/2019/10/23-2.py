import itertools
from heapq import heappop, heappush
from collections import defaultdict
def main(t, num):
    num = list(str(num))
    d = defaultdict(int)
    if t < sum(map(int, num)):
        print("error")
        return
    q = [[0,[]]]
    itertools.product()
    fulls = itertools.product(range(2), repeat=len(num) - 1)
    for full in fulls:
        tmp = 0
        res = []
        b = 0
        f = False
        for i in range(len(num) - 1):
            if full[i]:
                res.append(i)
                tmp += int("".join(num[b: i + 1]))
                b = i + 1
        tmp += int("".join(num[b:]))
        a, b = heappop(q)
        a *= - 1
        if a == tmp: d[a] += 1
        if t >= tmp > a:
            a = tmp
            b = res
        heappush(q, [-a, b])
    a, b = heappop(q)
    a *= - 1
    if d[a] or a == 0:
        print("rejected")
    else:
        ans = []
        be = 0
        for i in b:
            ans.append(int("".join(num[be: i + 1])))
            be = i + 1
        ans.append(int("".join(num[be:])))
        print(a,*ans)

if __name__ == "__main__":
    while 1:
        t, num = map(int, input().split())
        if t == num == 0:
            break
        main(t, num)
