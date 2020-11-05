from math import gcd
N = int(input())
A = list(map(int,input().split()))

g = 0
for a in A:
    g = gcd(g,a)
if g > 1:
    print('not coprime')
    exit()

sa = set(A)
if len(sa) < N:
    print('setwise coprime')
    exit()

MAXN = 10**6+10
sieve = [0,0] + [1]*MAXN
p = 2
small_primes = []
while p*p <= MAXN:
    if sieve[p]:
        small_primes.append(p)
        for q in range(2*p,MAXN+1,p):
            sieve[q] = 0
    p += 1

st = set()
for a in A:
    for p in small_primes:
        found = False
        while a%p==0:
            a //= p
            found = True
        if found:
            if p in st:
                print('setwise coprime')
                exit()
            st.add(p)
        if a==1: break
    else:
        if a in st:
            print('setwise coprime')
            exit()
        st.add(a)

print('pairwise coprime')
