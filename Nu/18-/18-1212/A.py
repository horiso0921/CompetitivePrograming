N = int(input())
Nb = N
SN = 0
for i in range(10):
    SN += N // (10 ** (9 - i))
    N = N % (10 ** (9 - i))
if Nb % SN == 0:
    print("Yes")
else:
    print("No")