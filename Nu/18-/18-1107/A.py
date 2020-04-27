N, M, X, Y = map(int, input().split())
a = list(map(int, input().split()))
for i in range(N):
    if(i == 0):
        mx= a[i]
    else:
        mx = max(a[i],mx)
a = list(map(int, input().split()))
if(mx >= Y):
    print("War")
    quit()
for i in range(M):
    if(i == 0):
        my = a[i]
    else:
        my = min(a[i],my)
if(my <= X):
    print("War")
    quit()
if(mx >= my):
    print("War")
else:
    print("No War")
