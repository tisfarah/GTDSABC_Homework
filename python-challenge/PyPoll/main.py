# importing the modules necessary to read in files
import os
import csv 

budget_file = os.path.join('Resources', 'election_data.csv')

# initializing empty list to put in the separate list based on column headers
voter= []
county = []
candidate = []

#import the file path as a csvfile and delimit by commas 
with open(budget_file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
   
    
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    # remove the headers from lists, 
    voter = voter[1:]
    county = county[1:]
    candidate = candidate[1:]

total_votes = len(voter)

# looked up how to extract unique values from list, set was most recommended 
candidate = set(candidate)
candidate =list(candidate)
#finding the total number each candidate won by looping through if statement and initializing counts 

Khan = 0
OTooley = 0
Correy = 0
Li =  0
for i in candidate:
    if i == "Khan":
        Khan += 1
    elif i == "O'Tooley":
        OTooley += 1
    elif i == "Correy":
        Correy += 1
    else:
        Li += 1
# finding the percentage of each candidate by dividng the total number by "total_votes"

Khan_pct = round((Khan/total_votes)*100)
OTooley_pct = round((OTooley/total_votes)*100)
Correy_pct = round((Correy/total_votes)*100)
Li_pct = round((Li/total_votes)*100)

print_stmt = (f"Election Results \n--------------------\nTotal Votes: {total_votes} \n--------------------\n {candidate[0]}: {Khan_pct}00% ({Khan}) \n {candidate[1]}: {OTooley_pct}00% ({OTooley}) \n {candidate[2]}:{Correy_pct}00% ({Correy})  \n {candidate[3]}: {Li_pct}00% ({Li}) \n--------------------\n Winner: \n--------------------\n")
print(print_stmt)


# Specify the file to write to
output_path = os.path.join("PyPollSummary_Farah.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile: # specify "w" for write, default is read

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    for line in print_stmt:
        csvfile.write(line)
