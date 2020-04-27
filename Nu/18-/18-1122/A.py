N = int(input())
def rk(n, memo):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = rk(n-1,memo) + rk(n-2,memo)
        return memo[n]
memo = [0 for i in range(87)]
print(rk(N, memo))