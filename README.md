# Election Analysis

## Election Audit Overview
#### A team from the Colorado Board of Elections requested assistance analyzing the results from a recent congressional election. By using Python, a script was created to analyze the .csv file provided by the Colorado Board of Elections. The script took data from the .csv file and through coding, output the election metrics to a .txt file for the Board of Elections to read. Below are the metrics the Board of Elections requested insight for:
1) Determine the total number of votes cast in the election.
2) Calculate the number of votes from each county.
3) Evaluate the percentage of total votes were present from each county.
4) Determine the county with the most votes cast.
5) Compile a list of all the candidates who received votes.
6) Determine how many total votes each candidate received.
7) Calculate the percentage of votes won by each candidate.
8) Establish the winning candidate based on the popular vote.

## Resources Utilized
##### Data Source: election_results.csv
##### Software: Python 3.7.6; Visual Studio Code 1.65.0

## Election Audit Results
#### Based on the data analyzed by the Python code, the following results were concluded for the election:
*	A total of 369,711 votes were cast for the election

*	The counties included in the election were:
     - Jefferson
     - Denver
     - Arapahoe
*	The vote numbers and vote percentages for each county are as follows:
     -	Jefferson county had 10.5% of the votes with a total of 38855 votes.
     -	Denver county had 82.8% of the votes with a total of 306,055 votes.
     -	Arapahoe county had 6.7% of the votes with a total of 24,801 votes.

***Denver county had the most votes cast with a total of 306,055 votes for a total of 82.8% of total votes.***



*	The candidates in the election were:
     - Charles Casper Stockham
     -	Diana DeGette
     -	Raymon Anthony Doane
*	Each candidate received the following votes and vote percentages:
     -	Charles Casper Stockham received 23.0% of the votes with 85,213 total votes.
     -	Diane DeGette received 73.8% of the votes with 272,892 total votes.
     -	Raymon Anthony Doane received 3.1% of the votes with 11,606 total votes.


***The winner of the election was Diane DeGette, who received 73.8% of votes with 272,892 total votes.***

## Election Audit Summary
While the results from this election audit appear to have limited insight as only three counties and three candidates were observed, the code created for this analysis can be applied to larger data sets and elections. If the Colorado Board of Elections were to analyze a different dataset, the code can be changed to analyze the different dataset from a different file by changing the file being loaded from “election_results.csv” to the new file. 
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
```
This would then import and analyze the data from the new file with the existing code. The Board of Elections could use this feature to run a similar analysis on other congressional campaigns to observe trends between candidate votes and county votes.

Additionally, the variables used in this script could be changed to variables that correlate to other election metrics, such as age of voters or voters’ political alignment. As seen below, the variables are defined near the beginning of the script and can be modified to fit the Board’s needs.
```
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}
```
Changing the datasets and variables are only two examples of how versatile this script is. The Colorado Board of Elections could utilize various other modifications to analyze their election data effectively and efficiently. 
