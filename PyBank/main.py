import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

num_rows = 0
total_profit = 0
total_list = []
months_list = []
previous_month = 0
change_calc = 0
change_list = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
        num_rows += 1
        total_profit += int(row[1])
        total_list.append(int(row[1]))
        months_list.append(str(row[0]))

    for i in range(len(total_list)):
        if i == 0:
            previous_month = total_list[i]
        else:
            change_calc = total_list[i] - previous_month
            change_list.append(change_calc) 
            previous_month = total_list[i]

length = len(change_list)
total = sum(change_list)

average = total / length
greatest_increase = max(change_list)
greatest_decrease = min(change_list)

increase_index = change_list.index(greatest_increase)
decrease_index = change_list.index(greatest_decrease)

for x in range(len(months_list)):
    if x == increase_index:
        increase_month = months_list[x+1]
    if x == decrease_index:
        decrease_month = months_list[x+1]

total_currency = "${:}".format(total_profit)
average_currency = "${:.2f}".format(average)
increase_currency = "${:}".format(greatest_increase)
decrease_currency = "${:}".format(greatest_decrease)

# print(num_rows)
# print(total_profit)
# print(average)
# print(greatest_increase)
# print(greatest_decrease)
# print(increase_month)
# print(decrease_month)

print("Financial Analysis")
print("------------------------------------------------")

print("Total months: " + str(int(num_rows)))
print("Total: " + str(total_currency))
print("Average Change: " + str(average_currency))
print("Greatest Increase in Profits: " + str(increase_month) + " " + "(" + str(increase_currency) + ")")
print("Greatest Decrease in Profits: " + str(decrease_month) + " " + "(" + str(decrease_currency) + ")")

output_file = os.path.join("PyBank_summary.txt")

with open(output_file, 'w') as f:
    print("Financial Analysis", file=f)
    print("------------------------------------------------", file=f)

    print("Total months: " + str(int(num_rows)), file=f)
    print("Total: " + str(total_currency), file=f)
    print("Average Change: " + str(average_currency), file=f)
    print("Greatest Increase in Profits: " + str(increase_month) + " " + "(" + str(increase_currency) + ")", file=f)
    print("Greatest Decrease in Profits: " + str(decrease_month) + " " + "(" + str(decrease_currency) + ")", file=f)



