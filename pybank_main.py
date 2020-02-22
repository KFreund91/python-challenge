import os
import csv

budget_csv = os.path.join("..",'python-challenge', 'budget_data.csv')

months = []
revenue = []
revenue_change = []
monthly_change = []

with open(budget_csv, 'r',newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

    total_months = len(months)
    total_pf = sum(revenue)
    
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    
    profit_increase = max(revenue_change)
    x = revenue_change.index(profit_increase)
    month_increase = months[x+1]
    
    profit_decrease = min(revenue_change)
    y = revenue_change.index(profit_decrease)
    month_decrease = months[y+1]

    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print(f"Total: $ {str(total_pf)}")
    print(f"Average Change: $ {str(round(monthly_change, 2))}")
    print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")