import math
print(math.factorial(10**5))
N = int(input())
s = list(input())
A = N - s
if A % 2 == 1:
    A -= 1
