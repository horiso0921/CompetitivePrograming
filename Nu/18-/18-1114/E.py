y = int(input())
m = int(input())
if(m == 1 or m == 2):
    y -= 1
    m += 12
d = int(input())
print(735369-(365*y+int(y/4)-int(y/100)+int(y/400)+int(306*(m+1)/10)+d-429))