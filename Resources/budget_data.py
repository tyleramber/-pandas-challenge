import os
import csv

rows = []
with open("PyBank/Resources/budget_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

data = [
    "Jan-10,1088983",
    "Feb-10,-354534",
    "Mar-10,276622",
    # Rest of the data...
]

months = []
profit_losses = []


for row in rows:
    months.append(row[0])
    profit_losses.append(int(row[1]))

# Calculate the total number of months
TOTAL_DATE = len(months)

# Calculate the net total amount of profit/losses
net_total = sum(profit_losses)

# Calculate the changes in profit/loss over the entire period
changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]

# Calculate the average of changes
average_change = sum(changes) / len(changes)

# Calculate the greatest increase in profits and corresponding month
max_increase = max(changes)
max_increase_index = changes.index(max_increase)
max_increase_month = months[max_increase_index + 1]

# Calculate the greatest decrease in profits and corresponding month
max_decrease = min(changes)
max_decrease_index = changes.index(max_decrease)
max_decrease_month = months[max_decrease_index + 1]

# Print the financial analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {TOTAL_DATE}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")