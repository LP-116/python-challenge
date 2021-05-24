import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

candidate_list = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0
lines = 0
percentage_dict = {}
all_votes = []


with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)
    
    for row in csv_reader:
        if row[2] not in candidate_list:
            candidate_list.append(str(row[2]))
            
        if row[2] == "Correy":
            Correy_votes += 1
        
        if row[2] == "Khan":
            Khan_votes += 1

        if row[2] == "O'Tooley":
            Otooley_votes += 1

        if row[2] == "Li":
            Li_votes += 1


all_votes = Khan_votes + Correy_votes + Li_votes + Otooley_votes

Correy_percentage = "{:.3f}%".format((Correy_votes / all_votes) * 100)
Khan_percentage = "{:.3f}%".format((Khan_votes / all_votes) * 100)
Otooley_percentage = "{:.3f}%".format((Otooley_votes / all_votes) * 100)
Li_percentage = "{:.3f}%".format((Li_votes / all_votes) * 100)

percentage_dict = {"Correy": Correy_percentage, "Khan": Khan_percentage, "O'Tooley" : Otooley_percentage, "Li" : Li_percentage,}

maximum = max(percentage_dict, key=percentage_dict.get)

print("Election Results")
print("------------------------------------------------")
print("Total Votes: " + str(int(all_votes)))
print("------------------------------------------------")
print("Khan:  " + str(Khan_percentage) + "  (" + str(Khan_votes) + ")")
print("Correy:  " + str(Correy_percentage) + "  (" + str(Correy_votes) + ")")
print("Li:  " + str(Li_percentage) + "  (" + str(Li_votes) + ")")
print("O'Tooley:  " + str(Otooley_percentage) + "  (" + str(Otooley_votes) + ")")
print("------------------------------------------------")
print("Winner: " + str(maximum))

output_file = os.path.join("Analysis", "PyPoll_summary.txt")

with open(output_file, 'w') as f:
    print("Election Results", file=f)
    print("------------------------------------------------", file=f)
    print("Total Votes: " + str(int(all_votes)), file=f)
    print("------------------------------------------------", file=f)
    print("Khan:  " + str(Khan_percentage) + "  (" + str(Khan_votes) + ")", file=f)
    print("Correy:  " + str(Correy_percentage) + "  (" + str(Correy_votes) + ")", file=f)
    print("Li:  " + str(Li_percentage) + "  (" + str(Li_votes) + ")", file=f)
    print("O'Tooley:  " + str(Otooley_percentage) + "  (" + str(Otooley_votes) + ")", file=f)
    print("------------------------------------------------", file=f)
    print("Winner: " + str(maximum), file=f)
