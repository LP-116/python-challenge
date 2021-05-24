import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

candidate_list = []
candidate_votes = {}

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
     
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(str(candidate_name))

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += candidate_votes[candidate_name]
    

# print(f'{candidate_list[candidate_name]} + {candidate_votes[candidate_name]})

print(candidate_votes)

all_votes = candidate_votes.values()
total_votes = sum(all_votes)

print(total_votes)

# for i in candidate_votes:
#     votes = candidate_votes.get(i)

# print(votes)



# all_votes = candidate1_votes + candidate2_votes + candidate3_votes + candidate4_votes

# candidate1_percentage = (candidate1_votes / all_votes) * 100

# print(candidate1_percentage)

# candidate2_percentage = (candidate2_votes / all_votes) * 100

# print(candidate2_percentage)

# candidate3_percentage = (candidate3_votes / all_votes) * 100

# print(candidate3_percentage)

# candidate4_percentage = (candidate4_votes / all_votes) * 100

# print(candidate4_percentage)

# print(all_votes)
# print(Khan_votes)
# print(Correy_votes)
# print(Li_votes)
# print(Otooley_votes)  
# print(candidate_list)


