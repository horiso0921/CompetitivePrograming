import shutil
while 1:
    i = int(input(">"))
    if i == -1:
        break
    make = r"C:\Users\crdjf\Desktop\Program\contest\ABC\{}".format(str(i))
    shutil.copytree(
        r'C:\Users\crdjf\Desktop\Program\contest\ABC\template', make)
