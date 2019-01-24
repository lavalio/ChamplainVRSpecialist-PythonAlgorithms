import csv

unique_types =set()
line_counter = 1
total_units_sold =0
europe_orders = 0

with open("Sales_Records.csv") as f:
    reader = csv.reader(f)

    for row in reader:

        if line_counter != 1:
            unique_types.add(row[2])
            total_units_sold +=int(row[8])

        if row[0] == "Europe":
            europe_orders += 1

        line_counter += 1

    print("Total Orders from Europe: {}".format(europe_orders))
    print("Total units Sold: {}".format(total_units_sold))
    print("")
    print("Here is unique item:")
    list_counter = 1
    for x in unique_types:
        print(str(list_counter)+"  "+x)
        list_counter +=1