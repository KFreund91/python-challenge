import os
import csv

election_csv = os.path.join("..",'python-challenge', 'election_data.csv')

voters = []
candidates = []


with open(election_csv, 'r',newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        voters.append(row[0])
        candidates.append(row[2])

total_votes_cast = len(voters)

per_Khan = round(candidates.count("Khan") / len(candidates) *100)
per_Correy = round(candidates.count("Correy") / len(candidates) *100)  
per_Li = round(candidates.count("Li") / len(candidates) *100) 
per_OTooley  = round(candidates.count("O'Tooley") / len(candidates) *100)

percentages = [per_Khan, per_Correy, per_Li, per_OTooley]



print("Election Results")
print("Total Votes:" + str(total_votes_cast))
print("Khan : " + str(candidates.count("Khan")) + ", " + str(per_Khan) + "%")
print("Correy : " + str(candidates.count("Correy")) + ", " + str(per_Correy) + "%")
print("Li : " + str(candidates.count("Li")) + ", " + str(per_Li) + "%")
print("O'Tooley : " + str(candidates.count("O'Tooley")) + ", " + str(per_OTooley) + "%")
print("Winner: " + str(max(percentages)))


file = open('output_pypoll.txt','w') 
 
file.write("Election Results") 
file.write("Total Votes:" + str(total_votes_cast)) 
file.write("Khan : " + str(candidates.count("Khan")) + ", " + str(per_Khan) + "%") 
file.write("Correy : " + str(candidates.count("Correy")) + ", " + str(per_Correy) + "%") 
file.write("Li : " + str(candidates.count("Li")) + ", " + str(per_Li) + "%")
file.write("O'Tooley : " + str(candidates.count("O'Tooley")) + ", " + str(per_OTooley) + "%")
file.write("Winner:" + str(max(percentages)))
 
file.close() 


        

        


        
    

    


   
    

    