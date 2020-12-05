#import os module & csv file
import os
import csv

#bring in csv file
election_data = os.path.join("election_data.csv")

#total number of counts
total_votes_cast = 0 

#list to capture the count of candidates 
candidates =[]

#list to capture percent of total votes for each candidate 
percent_votes = []

#list to capture total number of votes received for each candidate
number_votes = []

#opening and reading csv
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reading header
    csv_header = next(csvreader)

    for row in csvreader:
        #add to vote counter 
        total_votes_cast += 1

        #check the candidate column to generate "candidate list" and count the 
        #number of votes each candidate received.

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1    

    #add to percent list 
    for votes in number_votes:
        percentage = (votes/total_votes_cast) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" %  percentage
        percent_votes.append(percentage)

    #find winning candidate 
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candiate = candidates[index]

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes_cast)}")
print("-------------------------")
#loop to print out candidate names, percentage of votes and the total for each 
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candiate}")
print("-------------------------")
    
#export to txt
output = open("PyPoll_output.txt", "w")

line1 = "Election Results"
line2 = "-------------------------"
line3 = str(f"Total Votes: {str(total_votes_cast)}")
line4 = str("-------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line5 = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line5))
line6 ="-------------------------"
line7 = str(f"Winner: {winning_candiate}")
line8 = "-------------------------"
output.write('{}\n{}\n{}\n'.format(line6, line7, line8))