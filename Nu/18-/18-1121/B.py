w = input()
al = dict([(chr(i),0) for i in range(97, 97+26)])
for i in range(len(w)):
    al[w[i]] += 1
for keys,valuse in al.items():
    if valuse%2 != 0:
        print("No")
        quit()
print("Yes")
