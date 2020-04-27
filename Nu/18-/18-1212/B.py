N, A, B = map(int, input().split())
if N == 1 and A == B:
    print(1)
    quit()
if N < 2 or A > B:
    print(0)
else:
    AN = A * (N - 1) + B
    BN = A + (N - 1) * B
    print(BN-AN+1)