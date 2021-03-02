import shutil
while 1:
    i = int(input(">"))
    if i == -1:
        break
    make = r"C:\Users\horiu\Program\contest\ABC\{}".format(str(i))
    shutil.copytree(
        r'C:\Users\horiu\Program\contest\ABC\template', make)
