#A

"""
s = input().split("/")
if int(s[1]) <= 4:
    print("Heisei")
else:
    print("TBD")
"""
#B
"""
n = int(input())
ans = 0
for i in range(n):
    a = input().split()
    if a[1] == "JPY":
        ans += int(a[0])
    else:
        ans +=  float(a[0]) * 380000
print(ans)
"""

#C
import itertools

n, a, b, c = map(int, input().split())
abc = [a, b, c]
ans = float("INF")
x = [int(input()) for i in range(n)]
nums = list(itertools.product([0, 1, 2, 3], repeat = n))
#print(nums)
for i in nums:
    tmp = 0
    aa = 0
    ba = 0
    ca = 0
    for number, k in enumerate(i):
        if k == 1:
            if aa != 0:
                tmp += 10
            aa += x[number]
        if k == 2:
            if ba != 0:
                tmp += 10
            ba += x[number]
        if k == 3:
            if ca != 0:
                tmp += 10
            ca += x[number]
    if aa == 0 or ba == 0 or ca == 0:
        tmp = float("INF")
    else:
        tmp += abs(aa - a)
        tmp += abs(ba - b)
        tmp += abs(ca - c)
    ans = min(tmp, ans)
print(ans)
        
        
            


#D

"""
a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
s.sort()
t.sort()

import bisect


for i in range(q):
    x = int(input())
    s_l = bisect.bisect_left(s, x) - 1
    t_l = bisect.bisect_left(t, x) - 1
    s_r = s_l + 1
    t_r = t_l + 1
    if s_l == -1:
        s_l = 0
    if t_l == -1:
        t_l = 0
    if s_l == a :
        s_l = a - 1
        s_r = a - 1
    if s_r == a:
        s_r = a - 1
    if t_l == b:
        t_l = b - 1
        t_r = b - 1
    if t_r == b:
        t_r = b - 1
    ans = min(abs(t[t_l] - s[s_r]) + min(abs(t[t_l] - x), abs(s[s_r] - x)),
    abs(s[s_l] - t[t_r]) + min(abs(s[s_l] - x), abs(t[t_r] - x)),
    abs(s[s_l] - t[t_l]) + min(abs(s[s_l] - x), abs(t[t_l] - x)),
    abs(s[s_r] - t[t_r]) + min(abs(s[s_r] - x), abs(t[t_r] - x)),
    )
    
    print(ans)
"""
