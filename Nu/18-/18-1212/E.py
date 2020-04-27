N, L = map(int, input().split())
amida = []
check = [[0 for i in range(N*2)]for k in range(L)]
for i in range(L):
    amida.append(" " + input() + " ")
kotae = list(input())
for i in range(0, N* 2 , 2):
    if kotae[i] == "o":
        yoko = i + 1
tate = L-1
while tate != -1:
    if amida[tate][yoko - 1] == "-" and check[tate][yoko-1] == 0:
        check[tate][yoko-1] = 1
        yoko = yoko - 2
    elif amida[tate][yoko + 1] == "-" and check[tate][yoko+1] == 0:
        check[tate][yoko+1] = 1
        yoko = yoko + 2
    else:
        tate -= 1
print((yoko//2)+1)
            