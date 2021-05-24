import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

num_rows = 0
candidate_list = []
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0
lines = 0

# with open(election_csv) as csv_file:
#     csv_reader = csv.reader(csv_file)

#     csv_header = next(csv_reader, None)
    
#     for row1 in csv_reader:
#         if row1[2] not in candidate_list:
#             candidate_list.append(str(row1[2]))

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
        if row[2] not in candidate_list:
            candidate_list.append(str(row[2]))

            candidate1_votes = 0
            candidate2_votes = 0


    if row[2] == candidate_list[0]:
        candidate1_votes += 1
        
    if row[2] == candidate_list[1]:
        candidate2_votes += 1

        # if row[2] == candidate_list[2]:
        #     candidate3_votes += 1

        # if row[2] == candidate_list[3]:
        #     candidate4_votes += 1
    
    
print(candidate1_votes)
print(candidate2_votes)
# print(candidate3_votes)
# print(candidate4_votes)


# all_votes = candidate1_votes + candidate2_votes + candidate3_votes + candidate4_votes

# candidate1_percentage = (candidate1_votes / all_votes) * 100
# candidate2_percentage = (candidate2_votes / all_votes) * 100
# candidate3_percentage = (candidate3_votes / all_votes) * 100
# candidate4_percentage = (candidate4_votes / all_votes) * 100

# print(str(candidate_list[1]) + ": " + str(candidate1_percentage) + "(" + str(candidate1_votes) + ")")

# print(all_votes)
# print(Khan_votes)
# print(Correy_votes)
# print(Li_votes)
# print(Otooley_votes)  
# print(candidate_list)


