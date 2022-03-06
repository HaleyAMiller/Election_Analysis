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

                winning_candidate=candidate_name
# Using the with statment, open the file as a text file
with open(file_to_save,"w") as txt_file:

#Print the final vote count to the terminal
    election_results=(
        f"\nELection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
#Save the final vote count to the txt file
    txt_file.write(election_results)

    
    # Determine the percentage of votes each candidate won

    for candidate_name in candidate_votes:
            

            # Retrieve vote count of a candidate
            votes=candidate_votes[candidate_name]
            
    #         # Calculate percentage of votes
            vote_percentage=float(votes) / float(total_votes) * 100
            
    #     # Print candidate name and percentage of vote
            candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Re-formulate candidate_results
        #candidate_results=(f"{candidate_name}: {vote_percentage:.1f} ({votes:,})\n")
# Print each candidate, vote count, and percentage to the terminal
            #print(candidate_results)
# Save candidate results to our text file
            txt_file.write(candidate_results)

            if vote_percentage > winning_percentage:
                winning_percentage=vote_percentage

            candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
            
    #  # Determine winning vote count and candidate
    if (votes >= winning_count) and (vote_percentage >= winning_percentage):
            # If true set winning_count=votes and winning_percentage=vote_percentage
                #winning_count=votes
                #winning_percentage=vote_percentage
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
    txt_file.write(winning_candidate_summary)
