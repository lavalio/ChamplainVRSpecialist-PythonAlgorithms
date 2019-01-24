import csv

row_counter = 1
csv_data = [["Name", "Sex", "Age", "Height (Cent)", "Weight(kg)"]]

with open("biostats.csv","rt") as csv_file:
    reader = csv.reader(csv_file)


    for row in reader:
        if row_counter != 1:
            row[3] = round(float(row[3])*2.54)
            row[4] = round(float(row[4]) * 0.454)
            csv_data.append(row)
        row_counter += 1

with open('biostats_new.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)
    print("OK")


