##################
# Workshop 9-part1
##################
# Task 1
txt_file = open("ex9_sample.txt")
try:
    for line in txt_file:
        print(line.strip())

finally:
    txt_file.close()

# Task 2
# 1. using file open() format, try, for loop, finally file.close()
f1 = open("ex9_sample.txt", "r")
f2 = open("ex9_copy.txt", "w")
try:
    for line in f1:
        f2.write(line)
finally:
    f1.close()
    f2.close()

# 2. using open() as file
with open("ex9_sample.txt") as f1:
    with open("ex9_copy.txt", "w") as f2:
        for line in f1:
            f2.write(line)


# Task 3
import csv

file = open("ex9_cities.csv", "r")
try:
    csv_reader = csv.DictReader(file)
    total_sum = 0
    for row in csv_reader:
        # print("City:", row["city"], "Population:", row["population"])
        total_sum = total_sum + int(row["population"])
    print("Total population :", total_sum)

finally:
    file.close()

# Task 4
# import packages to read csv file and write to json file
# 2. Using file open(), try, for loop, finally file.close()
import csv, json

data = {}
csvFile = open("ex9_cities.csv", "r")
jsonFile = open("ex9_output.json", "w")
try:
    csv_reader = csv.DictReader(csvFile)
    for rows in csv_reader:
        record = rows["rank"]
        data[record] = rows

    jsonFile.write(json.dumps(data))
finally:
    csvFile.close()
    jsonFile.close()

# 2. Using with open() as file
import csv, json

csvFilePath = "ex9_cities.csv"
jsonFilePath = "ex9_output.json"

data = {}
with open(csvFilePath, "r") as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for rows in csv_reader:
        rank = rows["rank"]
        data[rank] = rows

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data))


##################
# Workshop 9-part2
##################
import csv

rank_header = "Rank"
city_header = "City"
pop_header = "Population"

file = open("ex9_cities.csv", "r")
try:
    csv_reader = csv.DictReader(file)

    i = 0
    for row in csv_reader:
        rank = int(row["rank"])
        city = row["city"]
        pop = int(row["population"])
        if i == 0:
            print(f"{rank_header:>4} {city_header:<20}{pop_header:>12}")
            print("=" * 37)
            print(f"{rank:>4} {city:<20}{pop:>12,d}")
        else:
            print(f"{rank:>4} {city:<20}{pop:>12,d}")
        i += 1
finally:
    file.close()
