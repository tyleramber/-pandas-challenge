import os
import csv

input_path = os.path.join("PyPoll","Resources", "election_data.csv")
   
rows =[]
with open(input_path, encoding="utf-8") as file:   
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
# Caluculate the total number of votes cast
votes = [row[2] for row in rows]
candidates = []

for name in votes: 
    if name not in candidates:
        candidates.append(name)

total_votes = len(rows)

# Extract the list of votes for each candidate
votes = [row[2] for row in rows]

# Extract the list of unique candidates
candidates = list(set(votes))

# Calculate and print the total number of votes and the list of candidates
print("Total votes:", total_votes)
print("List of candidates:", candidates)

totals = []
pcts = []
candidate_votes = {}

# Calculate and print the number of votes and percentage for each candidate
for candidate in candidates:
    total = votes.count(candidates)
    totals.append(total) # Append the total to the totals list
    pcts.append(total / total_votes) # Find pct and append to pcts list

# Count votes for each candidate
for row in rows:
    candidate = row[2]
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

for i in range(len(candidates)):
    print(f"{candidates[i]:28}  {totals[i]:16,.0f}  {pcts[i]:.02%}")

# name a winner    
for winner in candidates:
    winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
report = (
    f"{'Election Results': ^48}\n"
    f"{'-------------------------': ^48}\n"
    f"{'Total Votes:':<24}{total_votes:>0,.0f}\n"
    f"{'-------------------------': ^48}\n"
)

# Calculate and append the results for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    report += f"{candidate:<24}{percentage:.3f}% ({votes})\n"

report += (
    f"{'-------------------------': ^48}\n"
    f"{'Winner:':<24}{winner:>0}\n"
    f"{'-------------------------': ^48}"
)

print (report)
# Assemble the output text file path, starting from the cwd
output_path = os.path.join("PyPoll", "Analysis", "election_anylysis.txt")

# Open the budget_analysis text file and write the report to it
with open(output_path, "w", encoding="utf-8") as textfile:
    textfile.write(report)