car_inspections = [[True,False,True],
                   [True,True,True],
                   [False,False,False],
                   [True,True,True]]

count = 0

for car in car_inspections:
    count+=1
    print("Inspection for car number"+str(count))
    print("Inspector 1:" + str(car[0]))
    print("Inspector 2:" + str(car[1]))
    print("Inspector 3:" + str(car[2]))
    print()