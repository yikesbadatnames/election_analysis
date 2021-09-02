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
#create a dictionary for candidate votes
candidate_votes = {}
# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
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
            # begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            # add a vote to that candidates's count
        candidate_votes[candidate_name] += 1
    #deterine the percentage of botes for each candidate by looping through candidate vvotes dictionary
    # 1 iterate through the canddiate list
    for candidate_name in candidate_votes:
        #2 retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4 print the candidate name and percentage of votes
        print(f"{candidate_name}: recieved {vote_percentage}% of the vote.")
        # determine winning vote count and candidate
        #determine if the votes is greater than the winning count.
        if (votes> winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
            #print each candidate's name, vote count, and %
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
