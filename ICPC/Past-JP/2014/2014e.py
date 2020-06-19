from collections import defaultdict, deque

while 1:
    n = int(input())
    if n == 0:
        break
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))

    dic = defaultdict(int) 
    tree = [[] for i in range(n)]
    for i in range(n - 1):
        tree[i + 1].append(p[i]- 1)
        tree[p[i] - 1].append(i + 1)
        dic[(i + 1, p[i] - 1)] = d[i]
        dic[(p[i] - 1, i + 1)] = d[i]
    ans = 0
    de = []
    for num,i in enumerate(tree):
        if len(i) == 1:
            de.append((num,i[0]))
    for num, di in de:
        tree[num].remove(di)
        tree[di].remove(num)
        ans += dic[(num, di)]
    b = 0
    for i in range(n):
        check = [True] * n
        q = deque()
        q.append((i, 0))
        check[i] = False
        while q:
            now, di = q.pop()
            b = max(b, di)
            for k in tree[now]:
                if check[k]:
                    check[k] = False
                    q.append((k, di + dic[k, now]))
    print(sum(d)*3-2*ans-b)

