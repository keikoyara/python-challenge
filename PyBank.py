#import os module & csv file
import os
import csv

#creating variables out of csv file
budget_data = os.path.join("budget_data.csv")

#total number of months
total_months = 0
# net total profit/losses over entier period 
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
    

