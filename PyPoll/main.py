# setting up the script so that it runs in all operating systems and reads csv files
import os
import csv

# csv file location
election_csv = os.path.join("Resources","election_data.csv")

# lists and dictionaries that will be used in the script
candidate_list = []
candidate_votes = {}
percentage_list = []
all_votes = 0
total_votes = 0
name = []
votes = []

# opening the csv file and then skipping the first row in the file so that our headers aren't included in the calculations.
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

# defining what information we will be reading in the csv file. We will be looking at each row in column 3.
# We are now going through each row and determining the unqiue candidates in the column.
# Each time a candidate name appears in the column that has not been seen before, it adds it to a list called 'candidate_list'
# Once a new candidate has been identified an inital vote is placed against their name.
# When a candidate in the list has been identified, the votes get added to their name as an ongoing sum.

    for row in csv_reader:
     
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(str(candidate_name))

            candidate_votes[candidate_name] = 1
        else:      
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
# Next we add up all the votes counted by getting the values in the candidate_votes dictionary and then summing the values.

all_votes = candidate_votes.values()
total_votes = sum(all_votes)

# Next we take the candidate_votes dictionary and create 2 separate lists - one for the candidate names and one for their vote total.
# The lists are created in the order that they appear in the dictionary and therefore we can be confident that the first name in the list is paired with the first item in the value in the list.

name, votes = zip(*candidate_votes.items())

# Next we calculate the vote percentage.
# Using the range and len method, for each item in the votes list we divide the item by the total votes and convert to a percentage.
# We then create a new 'percentage' list for each number in the votes list. 
# The list is stored in the order that the item is added and therefore the alignment between candidate, total and vote percentage is aligned.

for x in range(len(votes)):
    percentage = "{:.3f}%".format((votes[x] / total_votes) * 100)
    percentage_list.append(str(percentage))

# Next we go back to the candidate vote dictionary and determine the biggest number in the dictionary and by extension the winner.

maximum = max(candidate_votes, key=candidate_votes.get)

# Then we print the results to the terminal.

print(" ")
print("Election Results")
print("------------------------------------------------")
print("Total Votes: " + str(int(total_votes)))
print("------------------------------------------------")

# To print the results of each candidate we combine the corresponding index in each list. ie. to get the first candidates result, we print the first value in each list.

for i in range(len(name)):
    print(str(name[i]) + ": " + str(percentage_list[i]) + " (" + str(votes[i]) + ")")

print("------------------------------------------------")
print("Winner: " + str(maximum))
print("------------------------------------------------")

# Finally, we print the results to a text file and save it in the 'Analysis' folder.

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
