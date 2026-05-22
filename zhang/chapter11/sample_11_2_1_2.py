import csv

with open("sample_11_2_1.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


