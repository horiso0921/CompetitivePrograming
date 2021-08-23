
#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def C():
    field = SR(8)
    check = [[0] * 8 for i in range(8)]
    
    def CK(check, Point):
        Check = [[check[i][j] for j in range(8)] for i in range(8)]
        y,x = Point
        if Check[y][x] == 1:
            return False
        Check[y][x] = 1
        for i in range(8):
            if i != x and field[y][i] == "Q":
                return False
            Check[y][i] = 1
        for i in range(8):
            if i != y and field[i][x] == "Q":
                return False
            Check[i][x] = 1
        for i in range(-8, 8):
            if i != 0:
                if 0 <= y + i < 8 and 0 <= x + i < 8:
                    if field[y + i][x + i] == "Q":
                        return False
                    Check[y + i][x + i] = 1
                if 0 <= y - i < 8 and 0 <= x + i < 8:
                    if field[y - i][x + i] == "Q":
                        return False
                    Check[y - i][x + i] = 1
        return Check
    
    for i in range(8):
        for k in range(8):
            if field[i][k] == "Q":
                check = CK(check, [i, k])
                #print(check)
                if not check:
                    print("No Answer")
                    return
    ans = []
    for i in range(8):
        for k in range(8):
            if not check[i][k]:
                ans.append([i, k])
    lenans = len(ans)
    numans = []
    
    def dfs(check, num, numans):
        bnumans = numans
        for i in range(num, lenans):
            Check = CK(check, ans[i])
            if Check:
                bnumans.append(i)
                if len(bnumans) == 5:
                    for i in bnumans:
                        field[ans[i][0]][ans[i][1]] = "Q"
                    return True
                if dfs(Check, i + 1, bnumans):
                    return True
                bnumans.remove(i)
        return False
    
    if dfs(check, 0, numans):
        for a in field:
            for b in a:
                print(b, end="")
            #print()
    else:
        print("No Answer")
        
if __name__ == '__main__':

#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
    a = LI()
    print(a)

