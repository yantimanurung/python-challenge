import os
import csv
import sys
csvpath = os.path.join('..', 'Pybank', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csvreader)
    total = 0
    months_count=0
    changes = []
    previous_month = 867884
    greatest_increase = 0
    greatest_decrease = 1926159
    for row in csvreader:
        total = total + int(row[1])
        months_count = months_count + 1
        monthly_changes = int(row[1]) - previous_month
        changes.append(monthly_changes)
        previous_month = int(row[1])
        if monthly_changes > greatest_increase:
            greatest_increase = monthly_changes
            increase_month = row[0]
        if monthly_changes < greatest_decrease:
            greatest_decrease = monthly_changes
            decrease_month = row[0]
            
    print(f'Financial Analysis')  
    print(f'--------------------------------') 
    print(f'Total Months: {months_count}')
    print(f'Total: {total}')
    change_total = 0
    for change in changes:
        change_total = change_total + change
    average_change = change_total/85
    average_change = round(average_change, 2)
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')
   

    sys.stdout = open('analysis.txt','wt')
    print(f'Financial Analysis')  
    print(f'--------------------------------') 
    print(f'Total Months: {months_count}')
    print(f'Total: {total}')
    change_total = 0
    for change in changes:
        change_total = change_total + change
    average_change = change_total/85
    average_change = round(average_change, 2)
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')
   