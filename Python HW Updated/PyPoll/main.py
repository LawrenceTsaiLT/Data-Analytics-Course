import os
import csv
import sys

csvpath = os.path.join('C:/Users/LT/Desktop/Python/election_data.csv')
with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    votes=[]
    next(csvreader)
    for row in csvreader:
        votes.append(row[0])

with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    khan_votes = 0
    for khan in csvreader:
        if khan[2] == "Khan":
            khan_votes += 1

with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    correy_votes = 0
    for correy in csvreader:
        if correy[2] == "Correy":
            correy_votes += 1

with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    li_votes = 0
    for li in csvreader:
        if li[2] == "Li":
            li_votes += 1

with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    otooley_votes = 0
    for otooley in csvreader:
        if otooley[2] == "O'Tooley":
            otooley_votes += 1
            
total_votes=len(votes)

Vote_Dictionary= {"Khan":khan_votes, "Correy":correy_votes, "Li":li_votes, "O'Tooley":otooley_votes}
print("Election Results")
print("-------------------------")
print("Total Votes: "+str(total_votes))
print("-------------------------")
print("Khan: "+str(round((khan_votes/total_votes)*100,2))+"% ("+str(khan_votes)+")")
print("Coorey: "+str(round((correy_votes/total_votes)*100,2))+"% ("+str(correy_votes)+")")
print("Li: "+str(round((li_votes/total_votes)*100,2))+"% ("+str(li_votes)+")")
print("O'Tooley: "+str(round((otooley_votes/total_votes)*100,2))+"% ("+str(otooley_votes)+")")
print("-------------------------")
print("Winner: "+max(Vote_Dictionary, key=Vote_Dictionary.get))
print("-------------------------")

sys.stdout = open('output.txt','wt')
print("Election Results")
print("-------------------------")
print("Total Votes: "+str(total_votes))
print("-------------------------")
print("Khan: "+str(round((khan_votes/total_votes)*100,2))+"% ("+str(khan_votes)+")")
print("Coorey: "+str(round((correy_votes/total_votes)*100,2))+"% ("+str(correy_votes)+")")
print("Li: "+str(round((li_votes/total_votes)*100,2))+"% ("+str(li_votes)+")")
print("O'Tooley: "+str(round((otooley_votes/total_votes)*100,2))+"% ("+str(otooley_votes)+")")
print("-------------------------")
print("Winner: "+max(Vote_Dictionary, key=Vote_Dictionary.get))
print("-------------------------")