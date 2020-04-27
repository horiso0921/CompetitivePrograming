n = int(input())
x = 0
y = 0
for i in range(n):
    a = list(input())
    x += a.count("X") * i
    y += a.count("Y") * (n-1-i)

if x > y:
    print("X")
elif y > x:
    print("Y")
else:
    print("Impossible")