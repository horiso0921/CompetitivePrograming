a = input()
A = 0
if a[0] == "A" and a[1].isupper() == False and a[-1].isupper() == False:
    for i in range(2,len(a)-1):
        if a[i] == "C" and A == 0:
	        A = 1
        elif a[i].isupper() == True:
            A = 2
if A == 1:
    print("AC")
else:
    print("WA")