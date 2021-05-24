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
percentage_list = []


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

all_votes = Khan_votes + Correy_votes + Li_votes + Otooley_votes

Khan_percentage = (Khan_votes / all_votes) * 100
Correy_percentage = (Correy_votes / all_votes) * 100
Li_percentage = (Li_votes / all_votes) * 100
Otooley_percentage = (Otooley_votes / all_votes) * 100

percentage_list = {"Khan": Khan_percentage, "Correy": Correy_percentage, "Li" : Li_percentage, "O'Tooley" : Otooley_percentage}

print(percentage_list)

# print(all_votes)
# print(Khan_votes)
# print(Correy_votes)
# print(Li_votes)
# print(Otooley_votes)  



