H, W = map(int, input().split())
C = [map(int, input().split()) for i in range(H)]
ans1 = [[0 for i in range(W/2)] for i in range(H/2)]
ans2 = [[0 for i in range(W/2)] for i in range(H/2)]
ans3 = [[0 for i in range(W/2)] for i in range(H/2)]
ans4 = [[0 for i in range(W/2)] for i in range(H/2)]
ANS = 0
NODE = 0
if(C[0][0] == 0 or C[0][W-1] == 0 or C[H-1][0] == 0 or C[H-1][0] == 0):
    ANS = 1

