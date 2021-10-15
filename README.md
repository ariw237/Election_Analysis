# Election_Analysis
## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election. The purpose of the election audit is to ascertain and perform the following from the election results:
1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. Determine the number votes cast in each county
7. Determine the percentage of votes cast in each county
8. Determine the county with largest voter turnout (votes cast)    

To obtain this data, a script has been written in Python (PyPoll_Challenge.py) to perform the analysis of the election data which is stored in the csv file in the resources folder.

## Resources
Data Source: resources_main/election_results.csv
Software: Python 3.7.0, Visual Studio Code

## Summary
### Election-Audit Results:
The Analysis show the following:
* There were 369,711 votes cast total
* The candidates were:  
   - Diane DeGette  
   - Raymon Anthony Doane  
   - Charles Casper Stockham   
* The candidate results were:  
  - Charles Casper Stockham received 23% of the vote and 85,213 votes total  
  - Diana DeGette received 73.8% of the vote and 272,892 votes total  
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes total  
* The winner of the election was:  
  - Diana DeGette who received 73.8% of the vote and 272,892 votes total
* The county results are as follows:  
  - There were three counties: Arapahoe, Jefferson, and Denver
  - 38,855 votes were cast in Jefferson county representing 10.51% of total votes
  - 24,801 votes were cast in Arapahoe county representing 6.71% of total votes
  - 306,055 votes were cast in Denver county representing 82.78% of total votes
  - Denver clearly had the highest voter turnout  
 
 The output from our Python script summarizes this nicely:  
 
 ![election](https://user-images.githubusercontent.com/60231630/137416134-d2d816ed-0db3-454b-aad9-0d256d89986d.png)  
 
 ###Election-Audit Summary  
The provided script is useful in the context of other elections as well. At the state level, this script can be modified for gubernatorial elections for state Governor by keeping track of ballots, candidates and counties. In this context, no modifications to the script are needed, however the resulting list of counties and ballots is likely to be quite large and execution of script may take longer. In the context of a local race for any public office this script is useful so long as counties are renamed based on the level from which votes are being cast.  For example, in a congressional race, we would be looking at various districts in our lists and dictionaries instead of counties. 
 
