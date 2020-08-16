with open("country list.txt", "r") as c:
    l = c.readlines()
alp = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for y in l:
    for x in alp:
        if x == y[0]:
            with open((str(x)+".txt"), "a") as b:
                b.write(y)
