X, Y = map(int, input().split("/"))
a = X / Y
import math
A = int(2 * X / Y)
B = int((4 * a - 1 + math.sqrt(16 * a ** 2 - 8 * a + 3)) / 2)
C = int((4 * a - 1 - math.sqrt(16 * a ** 2 - 8 * a + 3)) / 2)
if A > B:
    B = A
if A > C:
    print("Impossible")
    quit()
for i in range(B,C):
    ansa = (i * (i + 1) / 2) - (X * i / Y)
    if ansa.is_integer() and i != 0 and ansa > 0:
        print(i, int(ansa))
        break
else:
    print("Impossible")