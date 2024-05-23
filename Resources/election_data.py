import csv

with open("PyPoll/Resources/election_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = list(csvreader)
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
# print("Total votes:", total_votes)
# print("List of candidates:", candidates)

totals = []
pcts = []
candidate_votes = {}
total_votes = len(rows)

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
results= () 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

print(results)
