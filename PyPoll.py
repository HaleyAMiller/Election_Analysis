#Add our dependencies
import csv
import os
# Retrieve data to analyze
# Assign a variable to the file to load to and the path
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a filename avariable to save the file to a path
file_to_save=os.path.join("analysis","election_results.txt")
# Open the file and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here   
    # Read the file object with the reader function
    file_reader=csv.reader(election_data)

    headers=next(file_reader)
    print(headers)
    # Print each row in the csv file
    #for row in file_reader:
        #print(row)

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
