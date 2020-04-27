# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def gg(tama, fld):
    if(tama[0] == 1):
        fld[tama[1]+8*tama[2]] = 1
    elif(tama[0] == 2):
        fld[tama[1]+8*tama[2]] = 2
    ret(tama, fld)
    print(" ")
    return 0

def ret(tama, fld):
    x = tama[1] 
    y = tama[2]
    if(tama[1] != 0):
        for i in range(tama[1]-1, -1, -1):
            if(fld[i+8*y] == 0):
                break
            if(tama[0] == fld[i+8*y]):
                for k in range(tama[1]-1, i-1, -1):
                    fld[k+8*y] = tama[0]
                break
    if(tama[1] != 7):
        for i in range(tama[1]+1, 8):
            if(fld[i+8*y] == 0):
                break
            if(tama[0] == fld[i+8*y]):
                for k in range(tama[1]+1, i):
                    fld[k+8*y] = tama[0]
                break
    if(tama[2] != 0):
        for i in range(tama[2]-1, -1, -1):
            if(fld[x+8*i] == 0):
                break
            if(tama[0] == fld[x+8*i]):
                for k in range(tama[2]-1, i-1, -1):
                    fld[x+8*k] = tama[0]
                break
    if(tama[2] != 7):
        for i in range(tama[2]+1, 8):
            if(fld[x+8*i] == 0):
                break
            if(tama[0] == fld[x+8*i]):
                for k in range(tama[2], i):
                    fld[x+8*k] = tama[0]
                break
    if(tama[1] != 0):
        z = 1
        for i in range(tama[1]-1, -1, -1):
            if(y-z < 0):
                break
            if(fld[i+8*(y-z)] == 0):
                break
            if(tama[0] == fld[i+8*(y-z)]):
                j = 1
                for k in range(tama[1]-1, i-1,-1):
                    fld[k+8*(y-j)] = tama[0]
                    j += 1
                break
            z += 1
    if(tama[1] != 7):
        z = 1
        for i in range(tama[1]+1, 8):
            if(y+z > 7):
                break
            if(fld[i+8*(y+z)] == 0):
                break
            if(tama[0] == fld[i+8*(y+z)]):
                j = 1
                for k in range(tama[1]+1, i):
                    fld[k+8*(y+j)] = tama[0]
                    j += 1
                break
            z += 1
    if(tama[1] != 0):
        z = 1
        for i in range(tama[1]-1, -1, -1):
            if(y+z > 7):
                break
            if(fld[i+8*(y+z)] == 0):
                break
            if(tama[0] == fld[i+8*(y+z)]):
                j = 1
                for k in range(tama[1]-1, i-1, -1):
                    fld[k+8*(y+j)] = tama[0]
                    j += 1
                break
            z += 1
    if(tama[1] != 7):
        z  = 1
        for i in range(tama[1]+1, 8):
            if(y-z < 0):
                break
            if(fld[i+8*(y-z)] == 0):
                break
            if(tama[0] == fld[i+8*(y-z)]):
                j = 1
                for k in range(tama[1]+1, i):
                    fld[k+8*(y-j)] = tama[0]
                    j += 1
                break
            z += 1
    
x = int(input())
fld = []
b = 0
w = 0
for i in range(8*8):
    fld.append(0)
fld[3+8*4] = 1
fld[4+8*3] = 1
fld[3+8*3] = 2
fld[4+8*4] = 2
for i in range(x):
    tama = input()
    tama = tama.split()
    if(tama[0] == "B"):
        tama[0] = 1
    elif(tama[0] == "W"):
        tama[0] = 2
    tama[1] = int(tama[1])-1
    tama[2] = int(tama[2])-1    
    gg(tama, fld)
for i in range(64):
    if(fld[i] == 1):
        b += 1
    elif(fld[i] == 2):
        w += 1

if(b > w):
    print('{0:02d}-{1:02d} The black won!'.format(b,w))
elif(w > b):
    print('{0:02d}-{1:02d} The white won!'.format(b,w))
elif(w == b):
    print('{0:02d}-{1:02d} Draw!'.format(b,w))