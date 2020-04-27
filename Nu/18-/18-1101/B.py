def slv(a,i):
    if(a >= 2*10**12):
        return i
    else:
        return slv(a+(k*a)+1,i+1)
a, k = map(int, input().split())
if k == 0:
    print(2*10**12-a)
else:
    print(slv(a,0))