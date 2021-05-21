import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

num_rows = 0
total_profit = 0
total_variance = []
previous_month = 0
change_calc = 0
change_list = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_reader, None)

    for row in csv_reader:
        total_variance.append(int(row[1]))

    for i in range(len(total_variance)):
        if i == 0:
            previous_month = total_variance[i]
        else:
            change_calc = total_variance[i] - previous_month
            change_list.append(change_calc) 
            previous_month = total_variance[i]

        def average(change_list):
            length = len(change_list)
            total = 0
            for number in change_list:
                total += number
            return total / length

        print(average(change_calc))



