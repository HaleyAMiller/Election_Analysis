#Add our dependencies
import csv
import os
# Retrieve data to analyze
# Assign a variable to the file to load to and the path
file_to_load=os.path.join("Resources","election_results.csv")

# Assign a filename avariable to save the file to a path
file_to_save=os.path.join("analysis","election_results.txt")

# Initialize total vote counter.
total_votes=0

# Initialize candidate options list
candidate_options=[]

# Initialzie dictionary for each candidate's votes
candidate_votes={}

# Initalize winning candidate and winning count tracker
winning_candidate= " "
winning_count=0
winning_percentage=0

# Open the file and read the file
with open(file_to_load) as election_data:

# To do: read and analyze the data here   
    # Read the file object with the reader function
    file_reader=csv.reader(election_data)

    # Read the header row
    headers=next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:
            # Add to the total vote count
            total_votes += 1

            # Print the candidate name for each row
            candidate_name=row[2]

            # If the candidate name is not already listed, put in list
            if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
                candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count
                candidate_votes[candidate_name]= 0
        
        # Add to the candidate votes
            candidate_votes[candidate_name] += 1

            if candidate_votes[candidate_name] > winning_count:
                winning_count=candidate_votes[candidate_name]

# Determine the percentage of votes each candidate won
    for candidate_name in candidate_votes:
        

        # Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        
#         # Calculate percentage of votes
        vote_percentage=float(votes) / float(total_votes) * 100
        
#     # Print candidate name and percentage of vote
        #print(f"{candidate_name}: recieved {vote_percentage:.2f}% of the vote.")


        if vote_percentage > winning_percentage:
            winning_percentage=vote_percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
#  # Determine winning vote count and candidate
        if (votes >= winning_count) and (vote_percentage >= winning_percentage):
        # If true set winning_count=votes and winning_percentage=vote_percentage
            # winning_count=votes
            # winning_percentage=vote_percentage
            # # Set the winning_candidate=candidate_name
            winning_candidate=candidate_name
    # Print winning candidate, vote count, and percentage 
            winning_candidate_summary=(
            f"------------\n"
            f"Winner: {winning_candidate}\n"                    
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:,}"
            f"-----------\n")
            print(winning_candidate_summary)
            




    # Print candidate votes
    # print(candidate_votes)
    
    # Print candidate names
    #print(candidate_options)

    # Print total vote
    #print(total_votes)

# 1.Using the open() function with the "w" mode we will write data to the file
            #outfile=open(file_to_save,"w")
        #Write data to the file
            #outfile.write("Hello World!")
        #Close the file
            #outfile.close()
#2. Useing the with statment, open the file as a text file
#with open(file_to_save,"w") as txt_file:
#Write 3 counties to the file
    #Add counties on different lines
    #txt_file.write("Counties in the election:\n------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
#
#
#
