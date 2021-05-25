# setting up the script so that it runs in all operating systems and reads csv files
import os
import csv

# setting the csv path location
budget_csv = os.path.join("Resources","budget_data.csv")

# variables that will be used through the script
num_rows = 0
total_profit = 0
total_list = []
months_list = []
previous_month = 0
change_calc = 0
change_list = []

# opening the csv file and then skipping the first row in the file so that our headers aren't included in the calculations.
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

# Start looking at each row and determining how many rows there are and the total profit(by looking at column 2 of the csv file). 
# Generate a list showing each value in the profit/loss column and another list for the month column.
    for row in csv_reader:
        num_rows += 1
        total_profit += int(row[1])
        total_list.append(int(row[1]))
        months_list.append(str(row[0]))

# Next we go through the total profit/loss list and subtract one entry from the next to determine the monthly change in value. 
# The first entry in the list is the '0' position and therefore sets up the starting value.
# The variance is then calculated and a new list is created for the variance ('change_list').
# Once the change is calculated, the current entry becomes the previous months entry and the loop continues for all entries.

    for i in range(len(total_list)):
        if i == 0:
            previous_month = total_list[i]
        else:
            change_calc = total_list[i] - previous_month
            change_list.append(change_calc) 
            previous_month = total_list[i]

# Next we determine the length of the list of variances and sum the list entries. These results are then used to calculate the average.

length = len(change_list)
total = sum(change_list)
average = total / length

# Next we use max and min to determine the greatest profit and loss variance in the list.  

greatest_increase = max(change_list)
greatest_decrease = min(change_list)

# Next we find out the index of the greatest profit and loss in the list. 

increase_index = change_list.index(greatest_increase)
decrease_index = change_list.index(greatest_decrease)

# Next we use match the profit/loss indexes to the index in the month list
# Note that the month list will have an extra entry (since a variance for the first month is not calculated). 
# Therefore, to find the matching month we add 1 to the month index. 

for x in range(len(months_list)):
    if x == increase_index:
        increase_month = months_list[x+1]
    if x == decrease_index:
        decrease_month = months_list[x+1]

# Next we change the results into currency format.

total_currency = "${:}".format(total_profit)
average_currency = "${:.2f}".format(average)
increase_currency = "${:}".format(greatest_increase)
decrease_currency = "${:}".format(greatest_decrease)

# Then we print the results to the terminal.

print("  ")
print("Financial Analysis")
print("------------------------------------------------")

print("Total months: " + str(int(num_rows)))
print("Total: " + str(total_currency))
print("Average Change: " + str(average_currency))
print("Greatest Increase in Profits: " + str(increase_month) + " " + "(" + str(increase_currency) + ")")
print("Greatest Decrease in Profits: " + str(decrease_month) + " " + "(" + str(decrease_currency) + ")")

# Then we print the results to a text file and save it in the 'Analysis' folder.

output_file = os.path.join("Analysis", "PyBank_summary.txt")

with open(output_file, 'w') as f:
    print("Financial Analysis", file=f)
    print("------------------------------------------------", file=f)

    print("Total months: " + str(int(num_rows)), file=f)
    print("Total: " + str(total_currency), file=f)
    print("Average Change: " + str(average_currency), file=f)
    print("Greatest Increase in Profits: " + str(increase_month) + " " + "(" + str(increase_currency) + ")", file=f)
    print("Greatest Decrease in Profits: " + str(decrease_month) + " " + "(" + str(decrease_currency) + ")", file=f)



