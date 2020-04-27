D = list(map(int, input().split()))
J = list(map(int, input().split()))
score = 0
for i in range(7):
    score += max(D[i], J[i])
print(score)