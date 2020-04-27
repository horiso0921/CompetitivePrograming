N = int(input())
A = list(map(int, input().split()))
a = 0
ans = 1
def mod_combination(n, k, mod):
    # nCk (mod m)
    def mod_permutation(n, k, mod):
        if n<=k:
            return 1
        else:
            return (n * mod_permutation(n-1,k,mod))%mod

    def mod_inv_permutation(k, mod):
        k, mod = int(k), int(mod)
        if k<=1:
            return 1
        else:
            return (pow(k,mod-2,mod) * mod_inv_permutation(k-1, mod))%mod

    return (mod_permutation(n,n-k,mod) * mod_inv_permutation(k, mod))%mod
for i in range(N):
    if A[i] != -1:
        print(ans)
        ans *= mod_combination(A[i]-A[a]+1, i-a-1,10**9+7)
    
print(ans)

