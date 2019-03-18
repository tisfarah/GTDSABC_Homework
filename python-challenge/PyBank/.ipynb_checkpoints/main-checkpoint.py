# importing the modules necessary to read in files
import os
import csv 

budget_file = os.path.join('Resources', 'budget_data.csv')

# initializing empty list to put in the separate list based on column headers
months = []
profit_loss = []

#import the file path as a csvfile and delimit by commas 
with open(budget_file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(row[1])
    # remove the headers from both list, it was causing me errors when I tried to determine the Net P/L
    months = months[1:]
    profit_loss = profit_loss[1:]
# calculating the total number of months by using the length of the month list minus the header row
month_count = len(months)
month_count
type(month_count) # checking to see that month_count is a number 
# since the original profit loss list contains numerical values as strings versus float
#created for loop to convert the values to floats and sum to figure the Net Total of P/L over the entire period
profit_loss_float = []

for item in profit_loss:
    y = int(item)
    profit_loss_float.append(y)
    
NetPL = sum(profit_loss_float)

# finding the change between each set of 2 periods and putting that into a new list 

# initializing new list
MonthChangeList = []

# create a list that has pairs of the periods (i.e, (0,1), (1,2))
MonthPairs = zip(profit_loss_float[1:], profit_loss_float)

# loop through the pairs and find the difference for each pair (increase/decrease) and put to new list 
for a, b in MonthPairs:
    MonthChangeList.append(a-b)

#Average of the changes in profit/losses over the period is the average of the newly created list "MonthChangeList"
AvgChange = sum(MonthChangeList)/len(MonthChangeList)

#Greatest increase would be the MAX number in the MonthChangeList
MaxChange = max(MonthChangeList)

# Greatest decrease would be the MIN number in the MonthChangeLst
MinChange = min(MonthChangeList)
#Greatest increase would be the MAX number in the MonthChangeList
MaxChange = max(MonthChangeList)

#find the index of the Max value in the Months list
Max1 = MonthChangeList.index(1926159) 
# since the calculations for MonthChangelist were for pairs, find the hypothetical second index for the second item in the pair 
Max2 = Max1 + 1 

#find the months that correspond to the Max change value, the month that is assigned to the period of the second index "current" vs. "prior"
months[Max1]
months[Max2]

MaxPeriod = months[Max2]

# below is a check to see if I used the same indices in the profit/loss list that I used in the month list, will the current-prior calculation equate to the MaxChange number
profit_loss[Max1]
profit_loss[Max2]
float(profit_loss[Max2])-float(profit_loss[Max1])

# repeating the steps above for the Min number in the MonthChangeLost 
MinChange = min(MonthChangeList)
Min1 = MonthChangeList.index(-2196167)
Min2 = Min1 + 1
MinPeriod = months[Min2]

print_stmt = (f"Financial Analysis \n--------------------\nTotal Months: {month_count} \nTotal: ${NetPL} \nAverage Change: ${round(AvgChange,2)} \nGreatest Increase in Profits: {MaxPeriod} (${MaxChange}) \nGreatest Decrease in Profits: {MinPeriod} (${MinChange})")
print(print_stmt)

# Specify the file to write to
output_path = os.path.join("PyBankSummary_Farah.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile: # specify "w" for write, default is read

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    for line in print_stmt:
        csvfile.write(line)



