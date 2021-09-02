import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# assign a variable for the file to load and the path.
with open(file_to_load) as election_data:
#open the election results and read the file.
# to do: perform analysis
    print(election_data)
#close file
election_data.close()
#creat a file name variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
#using the with statement open the file as a text file
with open(file_to_save,"w") as txt_file:
#write some data to the file
    txt_file.write("Araphaoe\nDenver\nJefferson")
