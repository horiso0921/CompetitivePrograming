import sys, threading
sys.setrecursionlimit(10**7)
threading.stack_size(128*1024*1024)
def solve():
    n,q = map(int, input().split())
    if n == 0: return False
    par = [i for i in range(n)]
    check = [0] * n
    check[0] = 1
    for i in range(n-1):
        x = int(input())
        par[i+1] = x-1
    ques = [None] * q
    for i in range(q):
        que = input().split()
        if que[0] == "M":
            check[int(que[1]) - 1] += 1
        ques[i] = que
    
    def root(x):
        if check[x]: return x
        par[x] = root(par[x])
        return par[x]
    ans = 0
    for q, i in ques[::-1]:
        i = int(i) - 1
        if q == "M":
            check[i] -=1
        else:
            ans += root(i) + 1
    print(ans, flush=True)
    return True
def main():
    while solve():
        pass

threading.Thread(target=main).start()