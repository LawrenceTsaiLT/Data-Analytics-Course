import os
import csv

csvpath = os.path.join("C:/Users/LT/Desktop/Python/budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # use of next to skip first title row in csv file
    next(csvreader) 
    revenue = []
    date = []
    monthly_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])




    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_monthly_change = sum(monthly_change)/len(monthly_change)

        max_monthly_change = max(monthly_change)

        min_monthly_change = min(monthly_change)

        max_rev_change_date = str(date[monthly_change.index(max(monthly_change))])
        min_rev_change_date = str(date[monthly_change.index(min(monthly_change))])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(revenue))
    print("Average Change: $", round(avg_monthly_change))
    print("Greatest Increase in Profits:", max_monthly_change_date,"($", max_monthly_change,")")
    print("Greatest Decrease in Profits:", min_monthly_change_date,"($", min_monthly_change,")")