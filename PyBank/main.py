import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

num_rows = 0
total_profit = 0

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
        num_rows += 1
        total_profit += int(row[1])

    print(num_rows)
    print(total_profit)
