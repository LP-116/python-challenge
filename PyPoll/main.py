import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

num_rows = 0
candidate_list = []
lines = 0

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)
    lines = len(list(csv_reader))


with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)
    
    for row in csv_reader:
        if row[2] not in candidate_list:
            candidate_list.append(str(row[2]))


print(lines)           
print(candidate_list)


