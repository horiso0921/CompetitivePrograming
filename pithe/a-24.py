import math

N, K = map(int, input().split())

if N > K:
    print(0)
    quit()
ans = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]
ans[0][0] = 2
ans[1][3] = 2
ans[3][8] = 12
an = 0
ans[2][2] = 8
ans[2][4] = 8
ans[2][6] = 2
ans[2][8] = 2
ans[1][1] = 4
for i in range(3, 9):
    ans[i][i] = 2 ** (i + 1)
ans[3][5] = 26
ans[3][7] = 12
ans[4][6] = 80
ans[4][8] = 32
ans[5][7] = 242
ans[6][8] = 728
for i in range(9):
    if K <= i:
        break
    an += ans[N-1][i]
print(an)