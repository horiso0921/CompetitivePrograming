#A
"""
a,b = map(int, input().split())
if b % a == 0:
    print(b + a)
else:
    print(b-a)
"""

#B
"""
n, m = map(int, input().split())
ans = list(map(int, input().split()))
del ans[0]
ans = set(ans)
for i in range(n-1):
    a = list(map(int, input().split()))
    del a[0]
    ans = ans & set(a)
print(len(ans))
"""


#C
"""
import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

n = int(input())
a = list(map(int, input().split()))
print(gcd_list(a))
"""

#D
n,m = map(int, input().split())
a = list(map(int, input().split()))
num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
ans = [-float("inf") for _ in range(n + 1)]
num_ans = []
a.sort(reverse=True)
for i in a:
    num_ans.append(num[i])
ans[0] = 0
for i in range(n + 1):
    for b in num_ans:
        if i - b >= 0:
            ans[i] = max(ans[i - b] + 1, ans[i])
anse = ""
while ans[n] > 0:
    for k, i in enumerate(num_ans):
        if n - i >= 0:
            
            if ans[n] - 1 == ans[n - i]:
                anse += str(a[k])
                n -= i
                break
    if n < 0:
        break
            
print(anse)