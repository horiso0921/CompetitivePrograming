N, K = map(int, input().split())
A = [0 for _ in range(10 ** 5)]
for i in range(N):
    a, b = map(int, input().split())
    A[a - 1] += b
for i in range(10 ** 5):
    if K - A[i] > 0:
        K = K - A[i]
    else:
        print(i + 1)
        break