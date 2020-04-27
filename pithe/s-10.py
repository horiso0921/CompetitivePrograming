# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

dis = input()
dis = dis.split()
for i in range(len(dis)):
    dis[i] = int(dis[i])

number  = int(input())

total = 0
before = 0

for i in range(number):
    hantei = 0
    p = int(input())
    if(i != 0):
        if (dis[before] != p):
            if (before %2 == 0):
                for k in range(4):
                    if (dis[before-k-1] == p):
                        total += 1
                        hantei = 1
                        if (before-k-1 < 0):
                            before = before-k+5
                        else:
                            before = before-k-1
                    if (hantei == 0):
                        total +=2
                        before +=1
            elif (before %2 == 1):
                for k in range(4):
                    if (dis[before-k-2] == p):
                        total += 1
                        hantei = 1
                        if (before-k-2 < 0):
                            before = before-k+4
                        else:
                            before = before-k-2
                if (hantei == 0):
                    total +=2
                    before -=1
    print(before)
print(total)