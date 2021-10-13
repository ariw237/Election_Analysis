#Add necessary dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize number of votes
total_votes = 0
#Initialize empty list of candidates
candidate_list = []
#Initialize Votes by candidates in a dict
candidate_votes = {}
# Open the election results and read the file.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:


    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)  #Note the use of the reader method for csv module
    
    #read the header row using next function
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file. (Hashed out for now)
    for row in file_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
           #Add unique candidate name to list
           candidate_list.append(candidate_name)
           #Add votes for candidate
           candidate_votes[candidate_name] = 0
        #Print each row (hashed out):
        #print(row)  #Note how file reader references the file object and we iterate it
        #Count total number of votes
        total_votes += 1
        candidate_votes[candidate_name] += 1
#print(total_votes)
#print(candidate_list)
#print(candidate_votes)
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    for candidate in candidate_list:
        votes = (candidate_votes[candidate])
        vote_percentage = votes/(total_votes) * 100
        candidate_result = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_result)
        txt_file.write(candidate_result)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
        #print(f"{candidate}: received {vote_percentage:.2f}% of the vote.")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary) 
    txt_file.write(winning_candidate_summary)

    