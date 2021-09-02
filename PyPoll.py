import csv
import os
# assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
# set total_votes to 0 before opening file
total_votes = 0
# set candidate options to 0 before opening the file
candidate_options = []
# open the election results and read the file
with open(file_to_load) as election_data:
    #use csv.reader to look at the csv
    file_reader =  csv.reader(election_data)
    #read and print each header
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        # add a vote for each colmn
        total_votes = total_votes +1
            #print the candidate name for each row
        candidate_name = row[2]
        # if candidate name isn't already in candidate options...
        if candidate_name not in candidate_options:
        # add the candidate name to the candidate list 
            candidate_options.append(candidate_name)

#print total votes
print(total_votes)
#print candidate list
print(candidate_options)