def main(m, a, b):
    ans = [0,0,0]
    for x in p:
        for y in p:
            if x * y > m:
                break
            if 1 >= x / y >= a / b and x * y > ans[0]:
                ans = [x * y, x, y]
    print(ans[1], ans[2])

def primes(n):
    """ 
    Input n>=6, Returns a list of primes, 2 <= p < n 
    6以上の数であれば p (素数) <= n のlistを返す 
    :param int n:
    :rytpe list:
    """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

if __name__ == "__main__":
    p = primes(10000)
    while 1:
        m, a, b = map(int, input().split())
        if m == a == b == 0:
            break
        else:
            main(m,a,b)