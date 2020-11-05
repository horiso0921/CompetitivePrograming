from heapq import heappop, heappush
n = int(input())
s = input()
alp = [chr(ord("a") + i) for i in range(26)]
d = {}
for a in alp:
    d[a] = 0
for si in s:
    d[si] += 1
l = []
for i in range(26):
    if d[alp[i]]:
        heappush(l, (-d[alp[i]],alp[i]))
ans = [None] * n
for i in range(n):
    if i == 0:
        score, a = heappop(l)
        ans[i] = a
        if score + 1:
            heappush(l, (score + 1, a))
    elif i == 1:
        score, a = heappop(l)
        if ans[i-1] == a:
            if l:
                score1, a1 = heappop(l)
                heappush(l, (score, a))
                score = score1
                a = a1
            else:
                break
        ans[i] = a
        if score + 1:
            heappush(l, (score + 1, a))
    else:
        score, a = heappop(l)
        if ans[i-1] == a or ans[i-2] == a:
            if l:
                score1, a1 = heappop(l)
                if ans[i-1] == a1 or ans[i-2] == a1:
                    if l:
                        score2, a2 = heappop(l)
                        heappush(l, (score, a))
                        heappush(l, (score1, a1))
                        score = score2
                        a = a2
                    else:
                        break
                else:
                    heappush(l, (score, a))
                    score = score1
                    a = a1
            else:
                break
        ans[i] = a
        if score + 1:
            heappush(l, (score + 1, a))


if None in ans:
    print(-1)
else:
    print("".join(ans))