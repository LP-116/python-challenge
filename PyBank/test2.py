import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

num_rows = 0
total_profit = 0
total_list = []
previous_month = 0
change_calc = 0
change_list = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
        total_list.append(int(row[1]))

    for i in range(len(total_list)):
        if i == 0:
            previous_month = total_list[i]
        else:
            change_calc = total_list[i] - previous_month
            change_list.append(change_calc) 
            previous_month = total_list[i]

    
# length = len(change_list)
# total = sum(change_list)

# average = total / length

# print(average)
# print(change_list)

greatest_increase = max(change_list)
greatest_decrease = min(change_list)

print(greatest_increase)
print(greatest_decrease)