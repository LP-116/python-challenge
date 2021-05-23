import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

num_rows = 0
candidate_list = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0
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

        if row[2] == "Khan":
            Khan_votes += 1

        if row[2] == "Correy":
            Correy_votes += 1
        
        if row[2] == "Li":
            Li_votes += 1

        if row[2] == "O'Tooley":
            Otooley_votes += 1

 
print(Khan_votes)
print(Correy_votes)
print(Li_votes)
print(Otooley_votes)
print(lines)           
print(candidate_list)


