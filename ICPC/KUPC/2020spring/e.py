n = int(input())
a = [int(i) for i in input().split()]
s = sum(a)
m = min(a)
if s & 1 == 0 and m & 1 == 0:
    print("Second")
else:
    print("First")