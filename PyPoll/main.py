import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

candidate_list = []
candidate_votes = {}
percentage_list = []

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
     
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(str(candidate_name))

            candidate_votes[candidate_name] = 1
        else:      
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    

all_votes = candidate_votes.values()
total_votes = sum(all_votes)

name, votes = zip(*candidate_votes.items())

for x in range(len(votes)):
    percentage = "{:.3f}%".format((votes[x] / total_votes) * 100)
    percentage_list.append(str(percentage))

maximum = max(candidate_votes, key=candidate_votes.get)

# print(name)
# print(votes)
# print(percentage_list)
# print(maximum)

print(" ")
print("Election Results")
print("------------------------------------------------")
print("Total Votes: " + str(int(total_votes)))
print("------------------------------------------------")

for i in range(len(name)):
    print(str(name[i]) + ": " + str(percentage_list[i]) + " (" + str(votes[i]) + ")")

print("------------------------------------------------")
print("Winner: " + str(maximum))
print("------------------------------------------------")


output_file = os.path.join("Analysis", "PyPoll_summary.txt")

with open(output_file, 'w') as f:

    print("Election Results", file=f)
    print("------------------------------------------------", file=f)
    print("Total Votes: " + str(int(total_votes)), file=f)
    print("------------------------------------------------", file=f)

    for i in range(len(name)):
        print(str(name[i]) + ": " + str(percentage_list[i]) + " (" + str(votes[i]) + ")", file=f)

    print("------------------------------------------------", file=f)
    print("Winner: " + str(maximum), file=f)
    print("------------------------------------------------", file=f)
