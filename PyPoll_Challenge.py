# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources\election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
total_county_votes =0
# Candidate/county options and candidate/county votes
candidate_option =[]
county_option=[]
# declare the empty dictionary
candidate_votes ={}
county_votes={}

# Create an empty string that will hold the county name that had the largest turnout.
largest_county_turnout=""
largest_county_count=0
largest_county_percentage=0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
      

     # Read and print the header row.
    headers = next (file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate_option :
            # add the candidate name to the candidate list.
            candidate_option.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
             # begin tracking that candidate's vote count.
        candidate_votes[candidate_name] += 1
        
        # Add to the total vote count.
        total_county_votes += 1
        # Print the candidate name from each row.
        county_name = row[1]
        
        if county_name not in county_option :
        # add the candidate name to the candidate list.
            county_option.append(county_name)
        # Begin tracking that candidate's vote count.
            county_votes[county_name] = 0
                # begin tracking that candidate's vote count.
        county_votes[county_name] += 1

with open (file_to_save,"w")as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # print('REALLY OBVIOUS _____')
    # print(county_votes)
    for county in county_votes:
        Cvotes = county_votes[county]
        Cvotes_percentage = float(Cvotes)/float(total_county_votes)*100
        county_results = (
                f"{county}: {Cvotes_percentage:.1f}% ({Cvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        if (Cvotes > largest_county_count) and (Cvotes_percentage>largest_county_percentage):
            largest_county_count = Cvotes
            largest_county_percentage = Cvotes_percentage
            largest_county_turnout = county
    largest_county_string = "Largest County Turnout:" + str(largest_county_turnout) + "\n--------------------\n"
    print(largest_county_string)
    txt_file.write (largest_county_string)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        votes_percentage = float(votes)/float(total_votes)*100
        candidate_results = (
            f"{candidate}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (votes_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write (winning_candidate_summary)
