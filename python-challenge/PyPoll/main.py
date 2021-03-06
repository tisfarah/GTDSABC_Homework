# importing the modules necessary to read in files
import os
import csv 

election_file = os.path.join('Resources', 'election_data.csv')

# initializing empty list to put in the separate list based on column headers

election = {} 
voter = []
county = []
candidate2 = []

#import the file path as a csvfile and delimit by commas 
with open(election_file, ) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    csvreader = csv.DictReader(csv_file, delimiter = ",") # using the DictReader can reference using header name 
    for line in csvreader:
        if line["Candidate"] in election: # is candidate in dictionary
            election[line["Candidate"]] = election[line["Candidate"]] + 1
        else:
            election[line["Candidate"]] = 1
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    # remove the headers from lists, 
        voter = voter[1:]
        county = county[1:]
        candidate2 = candidate[1:]

           

#total_votes = len(voter)
total_votes = sum(election.values())

#print(total_votes)



# the dictionary keys contain the list of the candidates who got votes 

candidates = list(election.keys())
candidates
#finding the total number each candidate won by looping through if statement and
#initializing counts 

Khan = election.get("Khan")
OTooley = election.get("O'Tooley")
Correy = election.get("Correy")
Li =  election.get("Li")
      
#print(Li)


# finding the percentage of each candidate by dividng the total number by "total_votes"

Khan_pct = round((Khan/total_votes)*100)
OTooley_pct = round((OTooley/total_votes)*100)
Correy_pct = round((Correy/total_votes)*100)
Li_pct = round((Li/total_votes)*100)

#checking accuracy
type(Khan_pct)

# all_candidates = [Khan, OTooley, Correy, Li]
# max(all_candidates)

winner = max(election, key=election.get)

# max(election.values())

print_stmt = (f"Election Results \n--------------------\n Total Votes: {total_votes} \n--------------------\n {candidates[0]}:  {Khan_pct}.00% ({Khan}) \n {candidates[1]}: {Correy_pct}.00% ({Correy}) \n {candidates[2]}: {Li_pct}.00% ({Li}) \n {candidates[3]}: {OTooley_pct}.00% ({OTooley}) \n--------------------\n Winner: {winner}\n--------------------\n")

print(print_stmt)


# Specify the file to write to
output_path = os.path.join("PyPollSummary_Farah.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile: # specify "w" for write, default is read

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    for line in print_stmt:
        csvfile.write(line)
