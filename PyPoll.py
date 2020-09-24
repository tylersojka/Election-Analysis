# The data we need to retrieve:
# 1. The total number of votes
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


import csv
import os

#f = open("Resources/example.txt", "r")
# Open the election results and read the file
#results_file = os.path.join("Resources", "election_results.csv")
###with open(results_file, "r") as election_data:
#election_data = open("Resources/election_results.csv","r")

#print(*f)/print(f)
# To do: perform analysis.
    #print (election_data)

# Using the open() function with the "w" mode we will write data to the file.
#election_analysis = open("Analysis/election_analysis.txt", "r+")
# Create a filename variable to a direct or indirect path to the file.
#analysis_txt = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
##with open(analysis_txt, "w") as election_analysis:

    # Write some data to the file.
    ##election_analysis.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
    
results_file = os.path.join("Resources", "election_results.csv")
analysis_txt = os.path.join("Analysis", "election_analysis.txt")

with open(results_file) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)