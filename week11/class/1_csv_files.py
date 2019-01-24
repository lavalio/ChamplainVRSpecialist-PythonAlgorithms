import csv

row_counter = 1

with open("biostats.csv","rt") as csv_file:
    reader = csv.reader(csv_file)
    # next(reader)
    number_of_respondnets = 0
    total_age = 0
    females = 0

    for row in reader:
        if row_counter != 1:
            total_age += int(row[2])
            if row[1] =="F":
                females += 1


        row_counter += 1

    average_age = total_age/(row_counter-1)
    female_percentage = females/(row_counter-1)
    male_percentage = 1- female_percentage

print("Average_age: {}".format(average_age))
print("Female Percentage: {}".format(female_percentage))
print("Male Percentage: {}".format(male_percentage))



