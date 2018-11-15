times = 0
for a in range(2):
    p1 = a
    for b in range(2):
        p2 = b
        for c in range(2):
            p3 = c
            string = str(p1) + str(p2) + str(p3)
            times =  times + 1
            print(str(times) + ": " + string)


