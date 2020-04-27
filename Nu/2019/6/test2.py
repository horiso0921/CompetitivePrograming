import time

inf1 = 10 ** 20
inf2 = float("INF")
a = 0
b = 0
for i in range(10 ** 5):
    x = time.time()
    if 10 ** 19 > inf1:
        inf1 = inf1
    y = time.time()
    a += y - x
    x = time.time()
    if 10 ** 19 > inf2:
        inf2 = inf2
    y = time.time()
    b += y - x
print(a,b)