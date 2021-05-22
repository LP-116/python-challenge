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

print(num_rows)
print(total_profit)
print(average)
print(greatest_increase)
print(greatest_decrease)
print(increase_month)
print(decrease_month)
