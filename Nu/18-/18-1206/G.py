b = list(map(int, input().split()))
N = int(input())
a = []
import math
for i in range(N):
    a.append(int(input()))
a.sort()
a0 = [[], [], [], [], [], [], [], [], []]

for i in range(N):
    a0[int(math.log10(a[i]))].append(a[i])

for i in range(9):
    bf = a0[i]
    