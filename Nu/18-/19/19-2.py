# A
"""
n,k =map(int, input().split())

print(k * (k - 1)**(n - 1)) 
"""

# B

import math

r, n, m = map(int, input().split())

kankaku = 2 * r / n
tyusin = n / 2
sum = 0
for i in range(1, n + m):
    if i - m <= 0:
        yoko1 = 2*(r ** 2 - ((tyusin - i) * kankaku)** 2)**0.5
        sum += yoko1
    elif i > n:
        yoko2 = 2*(r ** 2 - ((tyusin - i + m) * kankaku)** 2)**0.5
        sum += yoko2
    else:
        yoko1 = 2 * (r ** 2 - ((tyusin - i) * kankaku)** 2)**0.5
        yoko2 = 2 * (r ** 2 - ((tyusin - i + m) * kankaku)** 2)**0.5
        sum += max(yoko1, yoko2)
print(sum)

# C
"""
n = int(input())
an = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += an[i] - 1
print(ans)
"""
# D
"""
import itertools
s = input()
sum = int(s)
sb = list(s)
for i in range(1, len(s)):
    a = list(itertools.combinations(list(range(1,len(s))), i))
    for k in a:
        sb = list(s)
        f = 0
        for n in k:
            sb.insert(n + f, "+")
            f += 1
        b = ""
        for n in sb:
            if n == "+":
                sum += int(b)
                b = ""
            else:
                b += n
        sum += int(b)

print(sum)
"""   