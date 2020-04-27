h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())

a = h1 * 60 + m1
b = h2 * 60 + m2

if a >= b:
    print("Yes")
else:
    if h2 < 6:
        print("Yes")
    else:
        if h2 - 6 < h1:
            print("Yes")
        else:
            if h2 - 6 == h1:
                if m2 <= 30:
                    print("Yes")
                else:
                    if m2 - 30 < m1:
                        print("Yes")
                    else:
                        print("No")
            else:
                print("No")

