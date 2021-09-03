#Importing Depedencies(?)---------------------------------------------------------------------
import csv
import os
#Command line -------------------------------------------------------------------------------
# assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
#Setting Values------------------------------------------------------------------------------
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
#Opening CSV ----------------------------------------------------------------
with open(file_to_load) as election_data:
    #use csv.reader to look at the csv
    file_reader =  csv.reader(election_data)
    #read and print each header
    headers = next(file_reader)
#Putting Candidate names in list ----------------------------------------------------------------
    #go through each row in the CSV 
    for row in file_reader:
        # add a vote for each colmn
        total_votes = total_votes +1
            #print the candidate name for each row !!! new variable
        candidate_name = row[2]
        # if candidate name isn't already in candidate options...
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list 
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count. add to dict
            candidate_votes[candidate_name] = 0
        # add a vote to that candidates's count
        candidate_votes[candidate_name] += 1 
        # saving results to our text file
        # with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\n Election Results \n"
        f"--------------------\n"
        f"Total Number of Votes = {total_votes:,}\n"
        f"--------------------\n"
    )
with open(file_to_save,"w") as txt_file:
    print(election_results, end = "")
    #saving in txt_file
    txt_file.write(election_results)

    #deterine the percentage of votes for each candidate by looping through candidate votes dictionary
    # 1 iterate through the canddiate list!!!!! assigning variables to keys in dictionary !!!!!
    for candidate_name in candidate_votes:
        #2 retrieve vote count of a candidate into dictonairy
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # determine winning vote count and candidate ---------------------------------------
        #determine if the votes is greater than the winning count.
        if (votes> winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
            #print each candidate's name, vote count, and %
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results,end="")
        txt_file.write(candidate_results)
    #winning candidate summary ----------------------------------------------------
    winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"
        )
    with open(file_to_save,"w") as txt_file:
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)