#Add necessary dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:


    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)  #Note the use of the reader method for csv module
    # Print each row in the CSV file. (Hashed out for now)
    #for row in file_reader:
    #    print(row)  #Note how file reader references the file object and we iterate it
    #print header row using next function
    headers = next(file_reader)
    print(headers)