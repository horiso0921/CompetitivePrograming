N = int(input())

a = (N // 10) * 100
b = (N % 10)
if b >= 7:
    print(a + 100)
else:
    print(a+b*15)