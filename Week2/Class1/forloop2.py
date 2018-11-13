star = " "

#for t in range(11):
for t in range(0,11):
    print(str(t)+":" + star)
    star = star + "*"

print("Program run has ended")



#Version 2

for y in range(0,11):
    print(str(y)+":", end = "" )
    for x in range(y):
        print("*",end = "")

print("Program run has ended")