# The data we need to retrieve
# open the election results and read the file
file_to_load = os.path.join("resources/election_results.csv")
# 1. The total number of votes cast
election_data = open(file_to_load,"r")
# 2. a complete list of candidates who recieved votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote





#Practice work for class
print(election_data)
#close the file
election_data.close()
#Example of Dependencies (datetime), Modeule (datetime), Package (now)
# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)