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
    
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2 Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# 3. Print the total votes.
#print(total_votes)
# Print the candidate list.
#print(candidate_votes)
