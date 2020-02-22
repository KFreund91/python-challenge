import os
import csv

election_csv = os.path.join("..",'python-challenge', 'election_data.csv')

votes = []






with open(election_csv, 'r',newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        votes.append(row[0])
        

        


        
    
    total_votes_cast = len(votes)
    

    print("Election Results")
    print("Total Votes:" + str(total_votes_cast))
   
    

    