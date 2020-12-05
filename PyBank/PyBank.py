#import os module & csv file
import os
import csv

#bring in csv file
budget_data = os.path.join("budget_data.csv")


total_months = 0
total_pl = 0
value = 0
changes = 0
dates = []
profits = []

#opening and reading CSV
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    #reading header
    csv_header = next(csvreader)
    
    #reading the first row 
    # += will give assigns new value to variable
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #going through each row after header & firt row
    for row in csvreader:

       #keep track of dates
       dates.append(row[0]) 

       #calculate the change, add it to list of changes 
       change = int(row[1])-value
       profits.append(change)
       value = int(row[1])

       #Total number of month
       total_months += 1
       
       #total net amount of profit/losses over time
       total_pl  = total_pl + int(row[1])
        
    #greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    
    #greatest decrease in profits
    greatest_decrease = min(profits)
    lowest_index = profits.index(greatest_decrease)
    lowest_date = dates[lowest_index]

    #average change in profit/loss
    avg_change = sum(profits)/len(profits)
    print(avg_change)

#display outputs
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change : ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})")

#out put to text file
output = open("PyBank_output.txt", "w")  

Lines = [
    "Financial Analysis \n",
    "---------------------------- \n",
    str(f"Total Months: {str(total_months)} \n"),
    str(f"Total: ${str(total_pl)} \n"),
    str(f"Average Change: ${str(round(avg_change,2))} \n"),
    str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)}) \n"),
    str(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)}) \n")
]

output.writelines(Lines)