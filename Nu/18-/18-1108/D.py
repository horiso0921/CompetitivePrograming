import bisect
L, R = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
r = list(map(int, input().split()))
r.sort()
score = 0
for i in range(10, 41):
    score += min(bisect.bisect_right(l, i)-bisect.bisect_left(l, i), bisect.bisect_right(r, i)-bisect.bisect_left(r, i))
print(score)